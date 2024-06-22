from django.shortcuts import render
from .models import * 

# Create your views here.

def all_websites(request): 

    websites = Website.objects.all() 

    context = {
        'websites': websites, 
    } 
    
    return render(request,'website/all-websites.html', context)


def website_details(request, id): 
    website = Website.objects.get(id=id) 


    context = {
        'website': website, 
    } 
    return render(request, 'website/website-details.html', context)