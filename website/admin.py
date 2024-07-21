from django.contrib import admin
from .models import * 
from django import forms
from django_ace import AceWidget


# Register your models here.
admin.site.register(Website)
admin.site.register(Database)

admin.site.register(DbTable)
admin.site.register(TableField)

class WebsitePageAdminForm(forms.ModelForm):
    class Meta:
        model = WebsitePage
        fields = '__all__'
        widgets = {
            'html': AceWidget(mode='html', theme='monokai', width='800px', height='400px'),
            'css': AceWidget(mode='css', theme='monokai', width='800px', height='400px'),
            'js': AceWidget(mode='javascript', theme='monokai', width='800px', height='400px'),
        }

class WebsitePageAdmin(admin.ModelAdmin):
    form = WebsitePageAdminForm

admin.site.register(WebsitePage, WebsitePageAdmin)