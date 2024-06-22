from django.shortcuts import render
from django.contrib import messages
from website.models import * 
from base.models import * 

# Create your views here.
def index(request): 

    websites = Website.objects.all() 
    tools = Tool.objects.all() 

    

    context = {
        'websites': websites, 
        'tools': tools, 
    } 

    # messages.add_message(request, messages.SUCCESS, message="رسالة تلقائية من الصفحة الرئيسية")

    return render(request, 'index.html', context)



def landing_page(request): 

    context = {} 
    return render(request, 'landing.html', context)