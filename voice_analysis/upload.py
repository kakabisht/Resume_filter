import sys
import time
import requests

filename = "/home/user/Desktop/sem 5/Project_SE/voice_analysis/elon_musk_neuralink.wav"
 
def read_file(filename, chunk_size=5242880):
    with open(filename, 'rb') as _file:
        while True:
            data = _file.read(chunk_size)
            if not data:
                break
            yield data
 
headers = {'authorization': "0f97c7d635494163b89cd968ec17ca3a"}
response = requests.post('https://api.assemblyai.com/v2/upload',
                         headers=headers,
                         data=read_file(filename))

print(response.json())