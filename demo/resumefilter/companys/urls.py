from django.urls import path
from . import views

app_name = 'companys'

urlpatterns = [
    path('', views.ListCompanys.as_view(), name="all"),
    path("new/", views.CreateCompany.as_view(), name="create"),
    path("applications/in/<slug>/",views.SingleCompany.as_view(),name="single"),
    path("join/<slug>/",views.JoinCompany.as_view(),name="join"),
    path("leave/<slug>/",views.LeaveCompany.as_view(),name="leave"),
]
