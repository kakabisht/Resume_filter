from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils.text import slugify
from accounts.models import User

# pip install misaka
import misaka

from django.contrib.auth import get_user_model
User = get_user_model()

# https://docs.djangoproject.com/en/2.0/howto/custom-template-tags/#inclusion-tags
# This is for the in_group_members check template tag
from django import template
register = template.Library()


class Company(models.Model):
    '''
    Responsible for storing name and description of the company
    '''
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(allow_unicode=True, unique=True)
    description = models.TextField(blank=True, default='')
    description_html = models.TextField(editable=False, default='', blank=True)
    members = models.ManyToManyField(User,through="CompanyMember")

    def __str__(self):       
        '''
        For the admin side, to unique indentify each company name        
        '''
        return self.name

    def save(self, *args, **kwargs):
        '''
        Saving the company details       
        '''
        self.slug = slugify(self.name)
        self.description_html = misaka.html(self.description)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        '''
        Unique page for details of a company
        '''
        return reverse("companys:single", kwargs={"slug": self.slug})

    class Meta:
        '''
        Sorting the companies by names        
        '''
        ordering = ["name"]


class CompanyMember(models.Model):
    '''
    Responsible for storing user and forms filled by the user for each company
    '''
    company = models.ForeignKey(Company,related_name='memberships',on_delete=models.CASCADE)
    user = models.ForeignKey(User,related_name='user_companys',on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    class Meta:
        '''
        An applicant and a company must be unique together       
        '''
        unique_together = ("company", "user")
