from elasticsearch import Elasticsearch

from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import credentials as cred

import dialogflow

import json
import os
import sys

# Check Elasticsearch connection
from elasticsearch import TransportError
try:
   es = Elasticsearch(cred.ES_HOST, http_auth=(cred.username, cred.password))
except TransportError as e:
    e.info()


application = Flask(__name__)
# Allow CORS Origin to perform requests from Angular project
CORS(application, resources={r"/api/*": {"origins": "*"}})


@application.route('/api/search/smart-agent/search/<term>', methods=['GET', 'POST'])
def send_message(term):
    """
    Method to send request to Dialogflow API & ES.
    The method returns json response according to the query return.
    """
    
    # print("Query term: " + term)
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = cred.chatbot_credentials
    project_id = cred.project_id
    session_id = cred.session_id
    language_code = cred.language_code

    chatbot_message = detect_intent_texts(
        project_id, session_id, term, language_code)

    # Return Json Response of the string message
    return jsonify(chatbot_message)


def detect_intent_texts(project_id, session_id, text, language_code):
    """
    Method to check if query term is found in Dialogflow and ES.
    The method returns the result in json string format.
    """

    import dialogflow_v2 as dialogflow
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)
    try:

        if text:
            text_input = dialogflow.types.TextInput(
                text=text, language_code=language_code)

            query_input = dialogflow.types.QueryInput(text=text_input)

            response = session_client.detect_intent(
                session=session, query_input=query_input)

            # (1) Check if query term found in Dialogflow API Intent == 'Default Welcome Intent'
            if response.query_result.intent.display_name == 'Default Welcome Intent':
                # print('Fulfillment text: {}\n'.format(response.query_result.fulfillment_text))
                dialogflow_message = {
                    "answer":
                    [{"_type": "dialog",
                        "message": response.query_result.fulfillment_text
                    }]}
                return dialogflow_message
                # (2) Check if query term found in Dialogflow API Intent == 'Default Fallback Intent'
            elif response.query_result.intent.display_name == 'Default Fallback Intent':
                # print('Fulfillment text: {}\n'.format(response.query_result.fulfillment_text))
                
                dialogflow_message = {
                    "answer":
                    [{"_type": "dialog",
                        "message": response.query_result.fulfillment_text
                    }]}
                return dialogflow_message
                
                # (3) Check if query term found in ES
            else:
                #print('Fulfillment text: {}\n'.format(response.query_result.fulfillment_text))
                elasticsearch_message = search_location_data(text)
                return elasticsearch_message
    
    except Exception as e:
        print('Error on line {}'.format(
        sys.exc_info()[-1].tb_lineno), type(e).__name__, e)


def search_location_data(term):
    #print("-" * 50)
    #print("Query term: " + term)
    result = es.search(
        index="restaurant",
        body={
            #"size": 3,
            "query": {
                "multi_match": {
                    "query": term,
                    "fields": ["name", "cuisine", "website", "email"]
                }
            },
            "_source": ["index", "restaurant_id", "name", "address", "locality", "region", "country", "latitude", "longitude", "tel", "website", "email", "cuisine", "price", "rating", "hours", "parking", "wifi"]
        })

    try:

        # Check if ES query returns more than 1 results
        if result["hits"]["total"]["value"] > 1:
            print("Yes query returned more than 1")
            print("Num of hits = " + str(result["hits"]["total"]["value"]))

            answers = []
            for data in result["hits"]["hits"]:

                # Check if index starts with "rest"
                if data["_index"].startswith("rest"):
                    _type = data["_index"][:4]
                    index = data["_index"]
                    address = data["_source"]["address"]
                    country = data["_source"]["country"]
                    
                    cuisine = []
                    for c in data["_source"]["cuisine"]:
                        cuisine.append(c)
                    email = data["_source"]["email"]

                    monday_hours = []
                    for mon in data["_source"]["hours"]["monday"]:
                        monday_hours.append(mon)
                    tuesday_hours = []
                    for tues in data["_source"]["hours"]["tuesday"]:
                        tuesday_hours.append(tues)
                    wednesday_hours = []
                    for wed in data["_source"]["hours"]["wednesday"]:
                        wednesday_hours.append(wed)
                    thursday_hours = []
                    for thrs in data["_source"]["hours"]["thursday"]:
                        thursday_hours.append(thrs)
                    friday_hours = []
                    for fri in data["_source"]["hours"]["friday"]:
                        friday_hours.append(fri)
                    saturday_hours = []
                    for sat in data["_source"]["hours"]["saturday"]:
                        saturday_hours.append(sat)
                    sunday_hours = []
                    for sun in data["_source"]["hours"]["sunday"]:
                        sunday_hours.append(sun)
                    
                    hours = {
                        "hours": {
                            "monday": monday_hours,
                            "tuesday": tuesday_hours,
                            "wednesday": wednesday_hours,
                            "thursday": thursday_hours,
                            "friday": friday_hours,
                            "saturday": saturday_hours,
                            "sunday": sunday_hours

                        }
                    }
                    latitude = data["_source"]["latitude"]
                    locality = data["_source"]["locality"]
                    longitude = data["_source"]["longitude"]
                    name = data["_source"]["name"]
                    parking = data["_source"]["parking"]
                    price = data["_source"]["price"]
                    rating = data["_source"]["rating"]
                    region = data["_source"]["region"]
                    restaurant_id = data["_source"]["restaurant_id"]
                    score = data["_score"]
                    tel = data["_source"]["tel"]
                    website = data["_source"]["website"]
                    wifi = data["_source"]["wifi"]
                      
                    answer = {
                        "_index": index,
                        "_type": _type,
                        "address": address,
                        "country": country,
                        "cuisine": cuisine,
                        "email": email,
                        "hours": hours,
                        "latitude": latitude,
                        "locality": locality,
                        "longitude": longitude,
                        "name": name,
                        "parking": parking,
                        "price": price,
                        "rating": rating,
                        "region": region,
                        "restaurant_id": restaurant_id,
                        "_score": score,
                        "tel": tel,
                        "website": website,
                        "wifi": wifi
                    }
                    answers.append(answer)

            
            chatbot_message = {"answer": answers}
            #print("Answer: ")
            #print(chatbot_message)

        # Check if ES query returns 1 result
        elif result["hits"]["total"]["value"] == 1:
            # print("Num of hits = " + str(result["hits"]["total"]["value"]))
            answers = []
            index = result["hits"]["hits"][0]["_index"]
            if index.startswith("rest"):
                _type = index[:4]
            score = result["hits"]["hits"][0]["_score"]
            restaurant_id = result["hits"]["hits"][0]["_source"]["restaurant_id"]
            name = result["hits"]["hits"][0]["_source"]["name"]
            address = result["hits"]["hits"][0]["_source"]["address"]
            locality = result["hits"]["hits"][0]["_source"]["locality"]
            region = result["hits"]["hits"][0]["_source"]["region"]
            country = result["hits"]["hits"][0]["_source"]["country"]
            latitude = result["hits"]["hits"][0]["_source"]["latitude"]
            longitude = result["hits"]["hits"][0]["_source"]["longitude"]
            tel = result["hits"]["hits"][0]["_source"]["tel"]
            website = result["hits"]["hits"][0]["_source"]["website"]
            email = result["hits"]["hits"][0]["_source"]["email"]
            cuisine = result["hits"]["hits"][0]["_source"]["cuisine"]
            price = result["hits"]["hits"][0]["_source"]["price"]
            rating = result["hits"]["hits"][0]["_source"]["rating"]
            hours = result["hits"]["hits"][0]["_source"]["hours"]
            parking = result["hits"]["hits"][0]["_source"]["parking"]
            wifi = result["hits"]["hits"][0]["_source"]["wifi"]
            answer = {
                "_index": index,
                "_type": _type,
                "score": score,
                "restaurant_id": restaurant_id,
                "name":  name,
                "address": address,
                "locality": locality,
                "region": region,
                "country": country,
                "latitude": latitude,
                "longitude": longitude,
                "tel": tel,
                "website": website,
                "email": email,
                "cuisine": cuisine,
                "price": price,
                "rating": rating,
                "hours": hours,
                "parking": parking,
                "wifi": wifi
            }
            answers.append(answer)

            chatbot_message = {"answer":  answers}
            #print("Answer: ")
            #print(chatbot_message)

        else:
            # Display error message
            chatbot_message = {
                "answer":
                [{"_type": "error",
                    "message": "Sorry I coud not find any relevant results! Please search again."
                  }]
            }

    except Exception as e:
        print('Error on line {}'.format(
            sys.exc_info()[-1].tb_lineno), type(e).__name__, e)

    # print("Answer: ")
    # print(chatbot_message)
    return chatbot_message

if __name__ == "__main__":
    application.debug = True  # it should be used only in development not production
    application.run()
