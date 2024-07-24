from django.contrib import admin
from .models import * 

# Register your models here.

admin.site.register(ProjectType)
admin.site.register(Project)
admin.site.register(FieldType)
admin.site.register(Field)