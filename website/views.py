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


def ajax_all_pages(request, id): 
    website = get_object_or_404(Website, id=id) 
    pages = WebsitePage.objects.filter(website=website) 

    context = {
        'website': website,
    }

    return render(request, 'ajax_all_pages.html', context)


def add_page(request): 
    if request.POST:
        website_id = request.POST.get('website_id') 
        website_obj = get_object_or_404(Website, id=website_id)
        page_name = request.POST.get('pageName')


        WebsitePage.objects.create(website=website_obj, name=page_name)

        print('website id') 
        print(website_id)

        print("="* 30) 
        print('page name') 
        print(page_name) 

        print('='* 30 ) 

        return ajax_all_pages(request, website_id)  