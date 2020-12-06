from django.urls import path
from . import views

app_name = 'companys'

urlpatterns = [
    # As as_view is used to display form as a view, 
    # classmethod as_view(**initkwargs)
    # Returns a callable view that takes a request and returns a response: 
    path('', views.ListCompanys.as_view(), name="all"),
    path("new/", views.CreateCompany.as_view(), name="create"),
    path("applications/in/<slug>/",views.SingleCompany.as_view(),name="single"),
    path("join/<slug>/",views.JoinCompany.as_view(),name="join"),
    path("leave/<slug>/",views.LeaveCompany.as_view(),name="leave"),
]
