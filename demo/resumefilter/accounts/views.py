from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.views.generic import CreateView
from . import forms

# Create your views here.
class SignUp(CreateView):
    form_class = forms.UserCreateForm
    # On a sucessful sign up it will take them to login
    success_url = reverse_lazy("login")
    # Template we need to use
    template_name = "accounts/signup.html"