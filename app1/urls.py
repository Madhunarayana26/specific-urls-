from django.urls import path
from app1.views import *
import app1
app_name='connection'
urlpatterns=[
    path('first/',first,name='first'),
    path('second/',second,name='second'),
    
]
