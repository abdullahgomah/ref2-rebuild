from django.contrib import admin
from .models import * 


class PageInline(admin.TabularInline): 
    model = ScreenField 

@admin.register(Page)
class PageAdmin(admin.ModelAdmin): 
    model = Page  
    list_filter = ('website', ) 

    inlines = [
        PageInline
    ]



admin.site.register(Website)
admin.site.register(ScreenFieldType)
admin.site.register(ScreenField)
admin.site.register(DbType)

admin.site.register(ExcelTemplate)


admin.site.register(PreBuiltField)