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

    class Meta:
        ordering = ['email']
     
    def __str__(self):
        return f"{self.email}"
    
    def save(self, *args, **kwargs):
        self.message_html = misaka.html(self.message)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse(
            "applications:single",
            kwargs={
                "username": self.user.username,
                "pk": self.pk
            }
        )

