from django.shortcuts import render

# Create your views here.
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
    fields = ("name", "description")
    model = Company

class SingleCompany(generic.DetailView):
    model = Company

class ListCompanys(generic.ListView):
    model = Company


class JoinCompany(LoginRequiredMixin, generic.RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse("companys:single",kwargs={"slug": self.kwargs.get("slug")})

    def get(self, request, *args, **kwargs):
        company = get_object_or_404(Company,slug=self.kwargs.get("slug"))

        try:
            CompanyMember.objects.create(user=self.request.user,company=company)

        except IntegrityError:
            messages.warning(self.request,("Warning, already a member of {}".format(company.name)))

        else:
            messages.success(self.request,"You are now a member of the {} company.".format(company.name))

        return super().get(request, *args, **kwargs)


class LeaveCompany(LoginRequiredMixin, generic.RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse("companys:single",kwargs={"slug": self.kwargs.get("slug")})

    def get(self, request, *args, **kwargs):
        try:
            membership = models.CompanyMember.objects.filter(
                user=self.request.user,
                group__slug=self.kwargs.get("slug")
            ).get()

        except models.CompanyMember.DoesNotExist:
            messages.warning(
                self.request,
                "You can't leave this company because you aren't in it."
            )

        else:
            membership.delete()
            messages.success(
                self.request,
                "You have successfully left this company."
            )
        return super().get(request, *args, **kwargs)
