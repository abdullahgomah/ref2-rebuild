from django.urls import path 
from .views import * 

app_name = 'page' 

urlpatterns = [
    path('', index, name='index'), 
]