from django.urls import path
from app1.views import *
app_name='someone1'

urlpatterns=[
    path('first/',first,name='first'),
]