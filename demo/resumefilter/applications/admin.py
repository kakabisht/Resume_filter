from django.contrib import admin
from . import models


# Register your models here.
class ApplicationMemberInline(admin.TabularInline):
    model = models.Application

admin.site.register(models.Application)
