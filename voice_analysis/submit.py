import requests

endpoint = "https://api.assemblyai.com/v2/transcript"

json = {
  "audio_url": "https://cdn.assemblyai.com/upload/39dd4a1c-8a13-4104-b9b4-5c18e72f674a"
}

headers = {
    "authorization": "0f97c7d635494163b89cd968ec17ca3a",
    "content-type": "application/json"
}

response = requests.post(endpoint, json=json, headers=headers)

print(response.json())
