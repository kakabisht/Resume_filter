import requests
import json
 
DANDELION_APP_ID = 'API KEY'
DANDELION_APP_KEY = 'API KEY'
 
SENTIMENT_URL = 'https://api.dandelion.eu/datatxt/sent/v1'
 
def get_sentiment(text, lang='en'):
    payload = {
        '$app_id': DANDELION_APP_ID,
        '$app_key': DANDELION_APP_KEY,
        'text': text,
        'lang': lang
    }
    response = requests.get(SENTIMENT_URL, params=payload)
    return response.json()
 
if __name__ == '__main__':
    query = "Hi, i am hridyesh singh bisht.I am a junior at Symbiosis institute of technology and I am passionate about technology specifically around the cloud domain."
    response = get_sentiment(query)
    print("The message sent to the API is {}".format(query))
    print(json.dumps(response, indent=4))