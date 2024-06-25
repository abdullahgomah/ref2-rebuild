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
    path('add-database/', add_database, name='add-database'), 
    path('db-details/<int:db_id>/', db_details, name='db-details'), 
    path('add-table/', add_table, name='add-table'), 
    path('del-table/<int:id>/', del_table, name='del-table'), 
]