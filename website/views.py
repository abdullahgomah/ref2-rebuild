from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages 
from .models import * 
from base.models import  *
# Create your views here.

def all_websites(request): 

    websites = Website.objects.all() 
    tools = Tool.objects.all() 

    context = {
        'websites': websites, 
        'tools': tools,     
    } 
    
    return render(request,'all-websites.html', context)


def website_details(request, id): 
    website = Website.objects.get(id=id) 


    context = {
        'website': website, 
    } 
    return render(request, 'website-details.html', context)


def ajax_all_websites(request): 
    websites = Website.objects.all() 

    context = {
        'websites': websites
    }

    return render(request, 'ajax_all_websites.html', context)

def create_new_website(request): 
    if request.POST:
        website_name= request.POST.get('websiteName')
        website_description = request.POST.get('websiteDescription') 
        website_tool = request.POST.get('websiteTool') 
        
        print("website name") 
        print(website_name)

        website_tool_obj = Tool.objects.get(id=website_tool)

        Website.objects.create(name=website_name, description=website_description, tool=website_tool_obj)


        return ajax_all_websites(request)
    

def del_website(request, id):
    website = get_object_or_404(Website, id=id) 
    website.delete() 
    
    msg = "تم حذف الموقع بنجاح"
    messages.add_message(request, messages.INFO, message=msg)

    return redirect('website:all-websites') 