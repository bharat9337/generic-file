from app.views import *
from django.urls import path
app_name='gn'

urlpatterns=[
    path('generic/',generic,name='generic'),
]