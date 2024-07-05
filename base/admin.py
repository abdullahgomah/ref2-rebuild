from django.contrib import admin
from .models import DBType, Tool, DbFieldType

# Register your models here.
admin.site.register(DBType)
admin.site.register(Tool)


class DbFieldTypeAdmin(admin.ModelAdmin): 
    list_filter = ('db_type', )

admin.site.register(DbFieldType, DbFieldTypeAdmin)
