from django.urls import path 
from .views import * 

app_name = 'app_v2' 

urlpatterns = [
    path('', index, name='index'), 
    path('<int:id>/', project_details, name='project-details' ), 
]