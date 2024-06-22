from django.urls import path 
from .views import * 

app_name = 'website' 

urlpatterns = [
    path('all/', all_websites, name='all-websites'),    
    path('<int:id>/', website_details, name='website-details'), 
    path('create/', create_new_website, name='create-new-website'), 
    path('ajax-all-websites/', ajax_all_websites, name='ajax-all-websites'), 
    path('del-websites/<int:id>/', del_website, name='del-website'), 
    path('add-page/', add_page, name='add-page'), 
]