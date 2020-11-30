import requests
import json

endpoint = "https://api.assemblyai.com/v2/transcript/1g8g4a97c-80a6-4740-9c5a-c8a8327fa090"

headers = {
    "authorization": "0f97c7d635494163b89cd968ec17ca3a",
}

response = requests.get(endpoint, headers=headers)
data_dict = response.json()
print('Audio duration {}'.format(data_dict["audio_duration"]))
print('Text {}'.format(data_dict["text"]))
print('Confidence {}'.format(data_dict["confidence"]))

# print(data_dict["text"])
# print(data_dict["confidence"])

# print(response.json())
# print(json.dumps(response.json(), indent=1))

