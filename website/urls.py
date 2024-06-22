from django.urls import path 
from .views import * 

app_name = 'website' 

urlpatterns = [
    path('all/', all_websites, name='all-websites'),    
    path('<int:id>/', website_details, name='website-details'), 
]