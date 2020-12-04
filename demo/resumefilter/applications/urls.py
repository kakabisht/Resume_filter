from django.urls import path
from . import views

app_name='applications'

urlpatterns = [
    path('', views.ApplicationList.as_view(), name="all"),
    path("new/", views.CreateApplication.as_view(), name="create"),
    path("by/<username>/",views.UserApplications.as_view(),name="for_user"),
    path("by/<username>/<int:pk>/",views.ApplicationDetail.as_view(),name="single"),
    path("delete/<int:pk>/",views.DeleteApplication.as_view(),name="delete"),

]
