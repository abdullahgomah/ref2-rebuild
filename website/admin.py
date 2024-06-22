from django.contrib import admin
from .models import * 

# Register your models here.
admin.site.register(Website)
admin.site.register(WebsitePage)
admin.site.register(Database)

admin.site.register(DbTable)
admin.site.register(TableField)
admin.site.register(FieldTypes)
