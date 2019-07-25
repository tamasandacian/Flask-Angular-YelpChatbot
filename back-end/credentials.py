import os

from dotenv import load_dotenv
from pathlib import Path

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

############################# CONNECTION TO ELASTICSEARCH LOCALHOST #################################
# username = os.environ.get('REPLACE_THIS_WITH_YOUR_ELASTICSEARCH_USERNAME')
# password = os.environ.get('REPLACE_THIS_WITH_YOUR_ELASTICSEARCH_PASSWORD')
# ES_HOST = "REPLACE_THIS_WITH_YOUR_ES_HOST"
############################# CONNECTION TO CLOUD ELASTICSEARCH #################################
username = os.environ.get('ELASTIC_CLOUD_USERNAME')
password = os.environ.get('ELASTIC_CLOUD_PASSWORD')
ES_HOST = "REPLACE_THIS_WITH_YOUR_ES_HOST"
############################# CONNECTION TO DIALOGFLOW API ######################################
project_id =  os.environ.get('PROJECT_ID')
session_id = os.environ.get('SESSION_ID')
language_code = os.environ.get('LANGUAGE_CODE')
chatbot_credentials = os.environ.get('CHATBOT_CREDENTIALS')
###################################################################################################                