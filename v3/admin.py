from django.contrib import admin
from .models import * 


@admin.register(Page)
class PageAdmin(admin.ModelAdmin): 
    model = Page  
    list_filter = ('website', ) 



admin.site.register(Website)
admin.site.register(ScreenFieldType)
admin.site.register(ScreenField)