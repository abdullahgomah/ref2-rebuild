from django.shortcuts import render
from website.models import * 

# Create your views here.
def index(request): 

    websites = Website.objects.all() 

    context = {
        'websites': websites, 
    } 

    return render(request, 'page/index.html', context)