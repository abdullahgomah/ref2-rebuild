from django import forms 
from django_ace import AceWidget 
from .models import WebsitePage

class WebsitePageForm(forms.ModelForm): 

    class Meta: 
        model = WebsitePage 
        fields = ['html', 'css', 'js']
        widgets = {
            'html': AceWidget(mode='html', theme='monokai'), 
            'css': AceWidget(mode='css', theme='monokai'), 
            'js': AceWidget(mode='javascript', theme='monokai'), 
        }
    # html = forms.CharField(widget=AceWidget(mode='html', theme='monokai'))
    # css = forms.CharField(widget=AceWidget(mode='css', theme='monokai'))
    # js = forms.CharField(widget=AceWidget(mode='js', theme='monokai'))
     