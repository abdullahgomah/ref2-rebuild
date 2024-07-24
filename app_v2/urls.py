from django.urls import path 
from .views import * 

app_name = 'app_v2' 

urlpatterns = [
    path('', main_interface, name='main-interface'), 
]