from elasticsearch import Elasticsearch
from elasticsearch import exceptions
from elasticsearch import connection

import mapping as mp
import credentials as cred
import json
import os
import sys

# Create elasticsearch instance
es = Elasticsearch(cred.ES_HOST, http_auth=(cred.username, cred.password))

class Indexer():
    """
    Class for creating restaurants mapping and ingest json data 
    from external file.
    """
    def create_mapping(self, index, body):
        """
        Method to create index for employees, project and skill.
        """
        try:
            es.indices.put_mapping(
                index=index, 
                doc_type="generated",
                body=body)
            print("-" * 50)
            print('Index created successfully!')
            
            return True
        except exceptions.RequestError:
            print("-" * 50)
            print('Index already exists')
            return False
        except Exception as e:
            print('-' * 50)
            print('An unknown error occured while connecting to Elasticsearch ...')
            print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)

    def index_data(self, input_file_path):
        """
        Method to ingest data to elasticsearch index.
        """
        try:
            with open(input_file_path) as f:
                json_data = json.loads(f.read())
                restaurant_id = 0
                for rest in json_data["restaurants"]:
                    restaurant_id +=  1
                    if "name" in rest:
                        name = rest["name"]
                    if "address" in rest:    
                        address = rest["address"]
                    if "locality" in rest:    
                        locality = rest["locality"]
                    if "region" in rest:
                        region = rest["region"]
                    if "country" in rest:
                        country = rest["country"]
                    if "latitude" in rest:
                        latitude = rest["latitude"]
                    if "longitude" in rest:    
                        longitude = rest["longitude"]
                    if "tel" in rest:
                        tel = rest["tel"]
                    if "fax" in rest:
                        fax = rest["fax"] 
                    if "website" in rest: 
                        website = rest["website"]
                    if "email" in rest:
                        email = rest["email"]

                    if "cuisine" in rest:    
                        cuisine = []
                        for c in rest["cuisine"]:
                            cuisine.append(c)

                    if "price" in rest:    
                        price = rest["price"]
                    if "rating" in rest:
                        rating = rest["rating"]
                    if "hours" in rest:

                        if "monday" in rest["hours"]:
                            monday_hours = []
                            for mon in rest["hours"]["monday"]:
                                monday_hours.append(mon)
                        if "tuesday" in rest["hours"]:
                            tuesday_hours = []
                            for tue in rest["hours"]["tuesday"]:
                                tuesday_hours.append(tue)
                        if "wednesday" in rest["hours"]:
                            wednesday_hours = []
                            for wed in rest["hours"]["wednesday"]:
                                wednesday_hours.append(wed)
                        if "thursday" in rest["hours"]:
                            thursday_hours = []
                            for thrs in rest["hours"]["thursday"]:
                                thursday_hours.append(thrs)
                        if "friday" in rest["hours"]:
                            friday_hours = []
                            for fri in rest["hours"]["friday"]:
                                friday_hours.append(fri)
                        if "saturday" in rest["hours"]:
                            saturday_hours = []
                            for sat in rest["hours"]["saturday"]:
                                saturday_hours.append(sat)
                        if "sunday" in rest["hours"]:
                            sunday_hours = []
                            for sun in rest["hours"]["sunday"]:
                                sunday_hours.append(sun)
                        
                        hours = {
                                "monday": monday_hours,
                                "tuesday": tuesday_hours,
                                "wednesday": wednesday_hours,
                                "thursday": thursday_hours,
                                "friday": friday_hours,
                                "saturday": saturday_hours,
                                "sunday": sunday_hours
                        }

                    if "parking" in rest:
                        parking = rest["parking"]
                    if "parking_garage" in rest:
                        parking_garage = rest["parking_garage"]
                    if "parking_street" in rest:
                        parking_street = rest["parking_street"]
                    if "parking_free" in rest:
                        parking_free = rest["parking_free"]
                    if "wifi" in rest:
                        wifi = rest["wifi"]
                    if "meal_breakfast" in rest:
                        meal_breakfast = rest["meal_breakfast"]
                    if "meal_deliver" in rest:
                        meal_deliver = rest["meal_deliver"]
                    if "meal_dinner" in rest: 
                        meal_dinner = rest["meal_dinner"]
                    if "meal_lunch" in rest:
                        meal_lunch = rest["meal_lunch"]
                    if "meal_takeout" in rest:
                        meal_takeout = rest["meal_takeout"]
                    if "options_healthy" in rest:
                        options_healthy = rest["options_healthy"]
                    if "options_organic" in rest:
                        options_organic = rest["options_organic"]
                    if "options_vegetarian" in rest:
                        options_vegetarian = rest["options_vegetarian"]
                    if "options_vegan" in rest:
                        options_vegan = rest["options_vegan"]
                    if "options_glutenfree" in rest:
                        options_glutenfree = rest["options_glutenfree"]
                    
                    # Ingest data to restaurant index
                    
                    restaurant = {
                        "restaurant_id": restaurant_id,
                        "name":  name,
                        "address": address,
                        "locality": locality,
                        "region": region,
                        "country": country,
                        "latitude": latitude,
                        "longitude": longitude,
                        "tel": tel,
                        "fax": fax,
                        "website": website,
                        "email": email,
                        "cuisine": cuisine,
                        "price": price,
                        "rating": rating,
                        "hours": hours,
                        "parking": parking,
                        "parking_garage": parking_garage,
                        "parking_street": parking_street,
                        "parking_free": parking_free,
                        "wifi": wifi,
                        "meal_breakfast": meal_breakfast,
                        "meal_deliver": meal_deliver,
                        "meal_dinner": meal_dinner,
                        "meal_lunch": meal_lunch,
                        "meal_takeout": meal_takeout,
                        "options_healthy": options_healthy,
                        "options_organic": options_organic,
                        "options_vegetarian": options_vegetarian,
                        "options_vegan": options_vegan,
                        "options_glutenfree": options_glutenfree
                    } 
                    
                    #print("-" * 50)
                    #print("Restaurant:")
                    #print(restaurant) 

                    es.index(index='restaurant', doc_type='generated', id=restaurant_id, body=restaurant)       
                    
                    if "reviews" in rest:
                        for review in rest["reviews"]:
                            if "review_website" in review:
                                review_website = review["review_website"]
                            if "review_url" in review:
                                review_url = review["review_url"]
                            if "review_title" in review:
                                review_title = review["review_title"]
                            if "review_text" in review:
                                review_text = review["review_text"]
                            if "review_rating" in review:
                                review_rating = review["review_rating"]
                            if "review_date" in review:
                                review_date = review["review_date"]

                            review = {
                                "restaurant_id": restaurant_id,
                                "review_website": review_website,
                                "review_url": review_url,
                                "review_title": review_title,
                                "review_text": review_text,
                                "review_rating": review_rating,
                                "review_date": review_date
                            }


                            #print("Review:")
                            #print(review)
                            es.index(index='review', doc_type='generated', body=review)


                    
        except Exception as e:
                print('Error occured while indexing data ...')
                print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)
                


if __name__ == "__main__":

    # Create elasticsearch mapping
    indexer = Indexer()
    indexer.create_mapping("restaurant", mp.restaurant_mapping)
    indexer.create_mapping("review", mp.review_mapping)

    # Index data to elasticsearch from specified directory
    input_file_path = path = "./mock_data/factual_tripadvisor_restaurant_data_all_100_reviews.json"
    indexer.index_data(input_file_path)
    print("Finished indexing data to Elasticsearch!")

        