# Yelp Chatbot Application
This project contains all the code necessary to reproduce Yelp Chatbot Application using Python3 Flask framework as REST API back-end service, Elasticsearch 7 and Angular 8 as client-side. 
Yelp Chatbot is an application that helps you participate in conversation using Dialogflow API and helps you find relevant information and business location accurately through the chat interface and Google Map API.

This project was developed using open-source data collection of 57 restaurants in the Bay Area of San Francisco and each restaurant having 100 reviews each. 
Moreover each restaurant data presents a large number of information taken from the Factual API or Yelp API and a 100 reviews taken from Trip Advisor. For more details navigate at the following url: https://www.kaggle.com/jkgatt/restaurant-data-with-100-trip-advisor-reviews-each 

Currently the project is still in development. More features will come.

![yelp_chatbot](https://user-images.githubusercontent.com/11573356/64729336-44e17d00-d4dd-11e9-8b8f-28a2c8aa159c.gif)

Core Functionalities:
```
- Search for business(es) location and details through multiple ES index fields:
     e.g. cuisine, name, website, email
- Display Chatbot answer(s) on query term
- Display Show More & Show Less button to display more or less information
- Display Google Map business location(s)
- Display Dialogflow conversation (Small Talk & Intents) through chat interface.
- Mobile friendly
```

Basic project installation steps:
```
Clone repository

BACK-END:
1. navigate to back-end project
   cd back-end

2. create virtual environment
   virtualenv -p python3 env
   source env/bin/activate

3. install all required libraries
   pip install -r requirements.txt

4. replace envars in .env file 
   
- use default credentials or create elastic cloud credentials
username = 'elastic'
password = 'changeme'

# (1) REPLACE ELASTICSEARCH CREDENTIALS 
ELASTICSEARCH_USERNAME_LOCALHOST='REPLACE_THIS_WITH_YOUR_ELASTICSEARCH_USERNAME'
ELASTICSEARCH_PASSWORD_LOCALHOST='REPLACE_THIS_WITH_YOUR_ELASTICSEARCH_PASSWORD'

- navigate to Google Cloud Platform
- create Google new project
   - get PROJECT_ID
- navigate to:
   -> API & Services -> Credentials -> Create credentials -> Service account key
   -> select Service account: Dialogflow Integrations 
   -> select key type: JSON
- download GOOGLE_APPLICATION_CREDENTIALS.json file

# (2) REPLACE DIALOGFLOW API CREDENTIALS
PROJECT_ID=REPLACE_THIS_WITH_YOUR_PROJECT_ID
SESSION_ID=REPLACE_THIS_WITH_YOUR_SESSION_ID
LANGUAGE_CODE=REPLACE_THIS_WITH_LANGUAGE_CODE
GOOGLE_APPLICATION_CREDENTIALS=REPLACE_THIS_WITH_PATH_TO_JSON_GOOGLE_APPLICATION_CREDENTIALS

- navigate to Dialogflow API 
- enable Intents
- create intents

5. Docker-elk
   git clone git@github.com:deviantony/docker-elk.git 
   cd docker-elk
   sudo docker-compose up

6. create restaurant, review indexes
   python3 indexer.py
   
   restaurant, review mappings can be found in
   mappings.py

7. run Flask application
   python3 application.py
   
FRONT-END:
1. cd front-end/smar-agent
2. npm install
3. navigate to front-end/smart-agent/src/app/app.module.ts
4. replace GOOGLE_MAP_CREDENTIALS
   AgmCoreModule.forRoot({
      apiKey: 'REPLACE_WITH_YOUR_GOOGLE_MAP_API_KEY'
    }),
5. ng serve
6. access locahost:4200 in browser

```

