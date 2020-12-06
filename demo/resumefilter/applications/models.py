import json
import sys
import time
import requests

# pip install misaka
import misaka

from django.db import models
from django.conf import settings
from django.urls import reverse

from companys.models import Company
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect, request
from django.shortcuts import redirect, render
from django.urls.base import reverse_lazy
User = get_user_model()

# For the text analysis
DANDELION_APP_ID = 'Auth id'
DANDELION_APP_KEY = 'Key id'

# Api end point
SENTIMENT_URL = 'https://api.dandelion.eu/datatxt/sent/v1'
 
def get_sentiment(text, lang='en'):
    '''
    For text analysis, takes in language as a parameter
    '''
    payload = {
        '$app_id': DANDELION_APP_ID,
        '$app_key': DANDELION_APP_KEY,
        'text': text,
        'lang': lang
    }
    # returns a json object
    response = requests.get(SENTIMENT_URL, params=payload)
    return response.json()
 
def read_file(filename, chunk_size=5242880):
    '''
    For uploading the file to the storage bucket online
    '''
    with open(filename, 'rb') as _file:
        while True:
            data = _file.read(chunk_size)
            if not data:
                break
            yield data



class Application(models.Model):
    '''
        Application model containing details of the application, along with data base restrictions and constraints
    '''
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
    text_sentiment_type=models.TextField(blank=True)
    text_sentiment_score=models.TextField(blank=True)

    

    class Meta:
        # How to order application in admin side
        ordering = ['email']
     
    def __str__(self):
        return f"{self.email}"

    
    def save(self, *args, **kwargs):
        '''
        Saving application form into the data base
        '''
        self.message_html = misaka.html(self.message)
        # filename = self.voice
        
        # For voice analysis Api
        headers = {'authorization': "token"}
        
        # Voice analysis API endpoint
        endpoint = "API end point"
        response = requests.get(endpoint, headers=headers)
        data_dict = response.json()

        # Text analysis method is used here and stored in the fields

        text_response = get_sentiment(self.message)

        self.text_sentiment_type=text_response["sentiment"]['type']
        self.text_sentiment_score=text_response["sentiment"]['score']


        print('Text analysis done for {}'.format(self.message))

        # Voice analysis method is used here and stored in the fields

        self.audio_duration=data_dict["audio_duration"]
        self.text=data_dict["text"]
        self.confidence=data_dict["confidence"] *100
        
        print('Voice analysis done for {}'.format(self.voice))
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        # To check information about a particular application
        return reverse(
            "applications:single",
            kwargs={
                "username": self.user.username,
                "pk": self.pk
            }
        )

