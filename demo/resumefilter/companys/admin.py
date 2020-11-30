from django.contrib import admin
from . import models

# Register your models here.

class CompanyMemberInline(admin.TabularInline):
    model = models.CompanyMember

admin.site.register(models.Company)
