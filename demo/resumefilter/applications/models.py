import json
import sys
import time
import requests

from django.db import models
from django.conf import settings
from django.urls import reverse


# pip install misaka
import misaka

from companys.models import Company

from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect, request
from django.shortcuts import redirect, render
from django.urls.base import reverse_lazy
User = get_user_model()

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
 
def read_file(filename, chunk_size=5242880):
        with open(filename, 'rb') as _file:
            while True:
                data = _file.read(chunk_size)
                if not data:
                    break
                yield data



class Application(models.Model):
    user = models.ForeignKey(User, related_name="applications",on_delete=models.CASCADE)
    company = models.ForeignKey(Company, related_name="applications",null=True, blank=True,on_delete=models.CASCADE)
    email = models.EmailField(max_length=254,unique=True)
    github=models.URLField(max_length=254,blank=True)
    linkedin=models.URLField(max_length=254,blank=True)
    portfolio_site=models.URLField(max_length=254,blank=True)
    resume=models.FileField(upload_to='resume/')
    voice=models.FileField(upload_to='audio/')
    message = models.TextField(max_length=254)
    message_html = models.TextField(editable=False)
    audio_duration=models.TextField(blank=True)
    text=models.TextField(blank=True)
    confidence=models.TextField(blank=True)
    text_sentiment=models.TextField(blank=True)
    

    class Meta:
        ordering = ['email']
     
    def __str__(self):
        return f"{self.email}"

    
    def save(self, *args, **kwargs):
        self.message_html = misaka.html(self.message)
        # filename = self.voice
        headers = {'authorization': "0f97c7d635494163b89cd968ec17ca3a"}
        # response = requests.post('https://api.assemblyai.com/v2/upload', headers=headers, data=read_file(filename))

        # print(response.json())
        # endpoint_dict = response.json()
        
        # print('Online Endpoint {}'.format(endpoint_dict["upload_url"]))
        # endpoint = endpoint_dict["upload_url"]

        endpoint = "https://api.assemblyai.com/v2/transcript/1g8g4a97c-80a6-4740-9c5a-c8a8327fa090"
        response = requests.get(endpoint, headers=headers)
        data_dict = response.json()
        text_response = get_sentiment(self.message)

        self.text_sentiment=text_response["sentiment"]

        print('Text analysis done for {}'.format(self.message))

        self.audio_duration=data_dict["audio_duration"]
        self.text=data_dict["text"]
        self.confidence=data_dict["confidence"]
        
        print('Voice analysis done for {}'.format(self.voice))
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse(
            "applications:single",
            kwargs={
                "username": self.user.username,
                "pk": self.pk
            }
        )

