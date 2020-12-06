from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.mixins import(
    LoginRequiredMixin,
    PermissionRequiredMixin
)
from django.urls import reverse
from django.db import IntegrityError
from django.shortcuts import get_object_or_404
from django.views import generic
from . models import Company,CompanyMember
from . import models

class CreateCompany(LoginRequiredMixin, generic.CreateView):
    '''
    Create a company Login is required
    '''
    fields = ("name", "description")
    model = Company

class SingleCompany(generic.DetailView):
    '''
    View details of a particular company using generic Detail view method
    '''
    model = Company

class ListCompanys(generic.ListView):
    '''
    View list of all companies using list view method
    '''
    model = Company


class JoinCompany(LoginRequiredMixin, generic.RedirectView):
    '''
    To fill the applicantion form for a company, Login is required  and redirect to confirmation of filling the form
    '''

    def get_redirect_url(self, *args, **kwargs):
        # To redirect to the particular company page
        return reverse("companys:single",kwargs={"slug": self.kwargs.get("slug")})

    def get(self, request, *args, **kwargs):
        # To get company form, if we can't then return a error stating you have already filled the form
        company = get_object_or_404(Company,slug=self.kwargs.get("slug"))

        try:
            CompanyMember.objects.create(user=self.request.user,company=company)

        except IntegrityError:
            messages.warning(self.request,("Warning, you have already filled the from for {}".format(company.name)))

        else:
            messages.success(self.request,"you have filled the from for {} company.".format(company.name))

        return super().get(request, *args, **kwargs)


class LeaveCompany(LoginRequiredMixin, generic.RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        # To redirect to the particular company page
        return reverse("companys:single",kwargs={"slug": self.kwargs.get("slug")})

    def get(self, request, *args, **kwargs):
        # To get company form, if we can't then return a error stating you have already filled the form
        try:
            membership = models.CompanyMember.objects.filter(
                user=self.request.user,
                group__slug=self.kwargs.get("slug")
            ).get()

        except models.CompanyMember.DoesNotExist:
            messages.warning(
                self.request,
                "You can't leave this company because you haven't filled the form for it."
            )

        else:
            membership.delete()
            messages.success(
                self.request,
                "You have successfully deleted the form this company."
            )
        return super().get(request, *args, **kwargs)
