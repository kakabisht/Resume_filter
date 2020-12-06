"""resumefilter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views 
 

urlpatterns = [
    # As as_view is used to display form as a view, 
    # classmethod as_view(**initkwargs)
    # Returns a callable view that takes a request and returns a response: 
    path('', views.HomePage.as_view(), name="home"),
    path('about/', views.AboutPage.as_view(), name="about"),
    path('admin/', admin.site.urls),
    path('accounts/', include("accounts.urls", namespace="accounts")),
    path('accounts/', include("django.contrib.auth.urls")),
    path('test/', views.TestPage.as_view(), name="test"),
    path('thanks/', views.ThanksPage.as_view(), name="thanks"),
    path('companys/',include("companys.urls", namespace="companys")),
    path('applications/', include("applications.urls", namespace="applications")),
]
