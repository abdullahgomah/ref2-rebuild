from django.urls import path 
from .views import * 

app_name = 'v3' 

urlpatterns = [
    path('', index, name='index'), 
    path("<int:id>/", website_details, name="website-details"), 
    path("page/<int:id>/", page_details, name='page-details'),
    path("page/<int:id>/export/", export_code, name='export-code'),
    path('page/<int:page_id>/upload_from_excel/', upload_from_execl, name='upload-from-excel')
]