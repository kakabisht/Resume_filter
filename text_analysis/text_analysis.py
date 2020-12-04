import requests
import json
 
DANDELION_APP_ID = '19d7dfce9682412690b939bc2e5aeb85'
DANDELION_APP_KEY = '19d7dfce9682412690b939bc2e5aeb85'
 
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
    query = "Hello, I am hridyesh singh bisht, and i am passionate about technology as i can get rich through it."
    response = get_sentiment(query)
    print(json.dumps(response, indent=4))