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
    model = models.Application
    select_related = ("user", "company")


class UserApplications(generic.ListView):
    model = models.Application
    template_name = "applications/user_application_list.html"

    def get_queryset(self):
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
    model = models.Application
    select_related = ("user", "company")

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(
            user__username__iexact=self.kwargs.get("username")
        )


class CreateApplication(LoginRequiredMixin, SelectRelatedMixin, generic.CreateView):
    # form_class = forms.ApplicationForm
    model = models.Application
    fields = ['user', 'company', 'email', 'github', 'linkedin', 'portfolio_site', 'resume', 'voice', 'message',]
    
    # def get_form_kwargs(self):
    #     kwargs = super().get_form_kwargs()
    #     kwargs.update({"user": self.request.user})
    #     return kwargs

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)
    


class DeleteApplication(LoginRequiredMixin, SelectRelatedMixin, generic.DeleteView):
    model = models.Application
    select_related = ("user", "company")
    success_url = reverse_lazy("applications:all")

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id=self.request.user.id)

    def delete(self, *args, **kwargs):
        messages.success(self.request, "Application Deleted")
        return super().delete(*args, **kwargs)

class Application_ThanksPage(TemplateView):
    template_name = "applications/application_thanks.html"
