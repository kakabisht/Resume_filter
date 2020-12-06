import requests
import json

endpoint = "end point"

headers = {
    "authorization": "API id",
}

response = requests.get(endpoint, headers=headers)
data_dict = response.json()
print(json.dumps(response.json(), indent=1))
print('Audio duration {} seconds'.format(data_dict["audio_duration"]))
print('Text: {}'.format(data_dict["text"]))
print('Confidence {} percent'.format(data_dict["confidence"]*100))
