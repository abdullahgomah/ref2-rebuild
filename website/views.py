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
    db_types = DBType.objects.filter(tool=website.tool) 

    context = {
        'website': website, 
        'db_types': db_types,
    } 
    return render(request, 'website-details.html', context)


def ajax_all_websites(request): 
    websites = Website.objects.all()[::-1]

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
    

def ajax_all_db(request, website_id): 
    website_obj = get_object_or_404(Website, id=website_id)

    databases = Database.objects.filter(website=website_obj)
    
    context = {
        'website': website_obj,
    } 
    return render(request, 'ajax_website_databases.html', context)

def add_database(request): 
    if request.POST: 
        website_id = request.POST.get('website_id')
        dbName = request.POST.get('dbName')
        dbType = request.POST.get("dbType")

        website_obj = get_object_or_404(Website, id=website_id)
        db_type_obj = get_object_or_404(DBType, id=dbType)

        Database.objects.create(website=website_obj, name=dbName, db_type=db_type_obj)

        return ajax_all_db(request, website_id=website_id)
    


def db_details(request, db_id): 
    db = get_object_or_404(Database, id=db_id) 

    context = { 
        'db': db 
    }

    return render(request, 'database-details.html', context)

def ajax_all_tables(request, db_id): 
    db_obj = get_object_or_404(Database, id=db_id) 

    context = {
        'db': db_obj   
    }
    return render(request, 'ajax-all-tables.html', context)
    

def add_table(request): 
    if request.POST: 
        db_id = request.POST.get('db_id') 
        table_name = request.POST.get('table_name') 

        print('='* 30)
        print(db_id) 
        print(table_name) 
        print('='* 30)


        db_obj = get_object_or_404(Database, id=db_id) 
        
        DbTable.objects.create(db=db_obj, name=table_name)

        return ajax_all_tables(request, db_id) 
    

def del_table(request, id): 
    table = get_object_or_404(DbTable, id=id) 
    print(table)  
    db_id = table.db.id 

    table.delete() 

    return ajax_all_tables(request, db_id)



def table_details(request, table_id): 
    table = DbTable.objects.get(id=table_id) 

    context = {
        'table': table, 
    }

    return render(request, 'table-details.html', context)