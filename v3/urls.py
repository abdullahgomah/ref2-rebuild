from django.urls import path 
from .views import * 

app_name = 'v3' 

urlpatterns = [
    path('', index, name='index'), 
    path("<int:id>/", website_details, name="website-details"), 
    path("page/<int:id>/", page_details, name='page-details'),
    path("page/<int:id>/export/", export_code, name='export-code'),
    path('page/<int:page_id>/upload_from_excel/', upload_from_execl, name='upload-from-excel'),
    path('del-field/<int:id>/', delete_screen_field, name='del-screen-field'),
    path("download-template/", download_excel_standard_file, name='download-template'),
    path("get-field-info/", get_field_info, name='get-field-info'), 
    path('fields-branch-interface/', fields_branch_interface, name='fields-branch-interface'), 
    path('fields-branch-interface/<int:id>/', single_tool_field_branch, name='single_tool_field_branch'), 
]