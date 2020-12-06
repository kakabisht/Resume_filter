import sys
import time
import requests

# The name of the file we have to sent to the API
filename = "/home/user/Desktop/sem 5/Project_SE/voice_analysis/elon_musk_neuralink.wav"
 
def read_file(filename, chunk_size=5242880):
    '''
    Reading the file
    '''
    with open(filename, 'rb') as _file:
        while True:
            data = _file.read(chunk_size)
            if not data:
                break
            yield data
 
# Auth token 
headers = {'authorization': "API ID"}
# Uploading the file to a cloud storage bucket
response = requests.post('https://api.assemblyai.com/v2/upload', headers=headers, data=read_file(filename))

print(response.json())