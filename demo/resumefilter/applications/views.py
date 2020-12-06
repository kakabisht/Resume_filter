from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import Http404, HttpResponse
from django.views import generic
from django.views.generic import TemplateView


# pip install django-braces
from braces.views import SelectRelatedMixin

from . import forms
from . import models

from django.contrib.auth import get_user_model
from . forms import ApplicationForm
from django.shortcuts import render
User = get_user_model()


class ApplicationList(SelectRelatedMixin, generic.ListView):
    '''
    List of all the applications using generic list view
    '''
    model = models.Application
    # Fields to be selected
    select_related = ("user", "company")


class UserApplications(generic.ListView):
    '''
    All the applications filled by the user
    '''
    model = models.Application
    template_name = "applications/user_application_list.html"

    def get_queryset(self):
        # Try to fetch all the applications by a username field
        try:
            self.application_user = User.objects.prefetch_related("applications").get(username__iexact=self.kwargs.get("username"))
        except User.DoesNotExist:
            raise Http404
        else:
            return self.application_user.applications.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["application_user"] = self.application_user
        return context


class ApplicationDetail(SelectRelatedMixin, generic.DetailView):
    '''
    A detailed view of a particular application using Detail View
    '''
    model = models.Application
    select_related = ("user", "company")

    def get_queryset(self):
        #filering the application
        queryset = super().get_queryset()
        return queryset.filter(
            user__username__iexact=self.kwargs.get("username")
        )


class CreateApplication(LoginRequiredMixin, SelectRelatedMixin, generic.CreateView):
    '''
    TO create a particular form, the user must be loged in and we use Create view 
    '''

    # Select the model and it's fields
    model = models.Application
    fields = ['user', 'company', 'email', 'github', 'linkedin', 'portfolio_site', 'resume', 'voice', 'message',]

    def form_valid(self, form):
        '''
        To validate the fields as well as to save the form
        '''
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)
    


class DeleteApplication(LoginRequiredMixin, SelectRelatedMixin, generic.DeleteView):
    '''
    TO delete a particular form, the user must be loged in and we use Create view 
    '''
    
    # Select the model and it's fields
    model = models.Application
    select_related = ("user", "company")
    success_url = reverse_lazy("applications:all")

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id=self.request.user.id)

    def delete(self, *args, **kwargs):
        #delete the application form
        messages.success(self.request, "Application Deleted")
        return super().delete(*args, **kwargs)

class Application_ThanksPage(TemplateView):
    '''
    When the user has logged out of the application
    '''
    template_name = "applications/application_thanks.html"
