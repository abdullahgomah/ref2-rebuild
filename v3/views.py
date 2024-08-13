from django.shortcuts import render, get_object_or_404, redirect
from .models import * 
from urllib.parse import quote
from django.http import HttpResponseRedirect
from django.http import HttpResponse
import os 
from zipfile import ZipFile
from openpyxl import load_workbook

# Create your views here.

def index(request):

    """
        index page contains all websites 
        add new website 
    """

    if request.POST:
        name = request.POST.get('website-name-input') 
        url= request.POST.get('website-url-input') 
        description = request.POST.get('description-input') 
        dbtype = request.POST.get('dbtype-input')
        dbtype_obj = DbType.objects.get(name=dbtype) 

        if name != "" or name != None: 
            Website.objects.create(
                name = name, 
                url = url,
                description= description,
                db_type=dbtype_obj
            )


    websites = Website.objects.all() 
    dbtypes = DbType.objects.all() 

    context = {
        'websites': websites,
        'dbtypes': dbtypes, 
    } 
    return render(request, 'v3/index.html', context)


def website_details(request, id):
    website = get_object_or_404(Website, id=id)

    if request.POST: 
        page_name = request.POST.get('page-name-input') 
        
        Page.objects.create(
            website=website, 
            name= page_name 
        )

        return redirect('v3:website-details', id=id) 



    context ={
        'website': website, 
    }
    return render(request, 'v3/website-details.html', context)


def page_details(request, id): 

    page = get_object_or_404(Page, id=id) 
    sf_types = ScreenFieldType.objects.all() 

    if request.POST: 
        sf_type_input = request.POST.get('sf_type-input') 
        field_name = request.POST.get('field-name-input') 

        sf_type_obj = ScreenFieldType.objects.get(name=sf_type_input)

        ScreenField.objects.create(
            page=page, 
            sf_type=sf_type_obj, 
            name=field_name 
        )

        return redirect('v3:page-details', id=id) 


    context = {
        'page': page, 
        'sf_types': sf_types, 
    } 
    return render(request, 'v3/page-details.html', context)



def export_code(request, id): 
    page = get_object_or_404(Page, id=id)

    # filename = f"{page.name}.txt"
    names = [
        f"{page.name}.txt", 
        f"{page.name}.html"
    ]
    

    for filename in names: 
    
        with open(filename, 'w+', encoding='utf-8') as code: 
            for field in page.s_fields.all(): 
                cmd = field.sf_type.cmd 
                cmd = str(cmd)

                code.write(cmd) 
                code.write('\n')


    
    output_zipfile_name = f"{page.website.id}output-{page.id}.zip"

    with ZipFile(output_zipfile_name, 'w') as zip_object: 
        for name in names: 
            zip_object.write(name)


    with open(output_zipfile_name, 'rb') as f: 
        file_content = f.read() 

    # response = HttpResponse(file, content_type="text/html")
    # response['Content-Disposition'] = f'attachment; filename="{filename}"'
    
    # return response


    # URL encode the filename to ensure compatibility
    encoded_filename = quote(output_zipfile_name)

    # Create the HTTP response to download the file
    response = HttpResponse(file_content)
    response['Content-Type'] = 'application/x-zip-compressed'
    # response['Content-Disposition'] = f'attachment; filename*=UTF-8\'\'{encoded_filename}'
    response['Content-Disposition'] = f'attachment; filename={encoded_filename}'

    os.remove(output_zipfile_name) 
    
    return response


def upload_from_execl(request, page_id): 
    page = get_object_or_404(Page, id=page_id)

    if request.POST: 
        file = request.FILES['file-input']
        wb = load_workbook(filename=file) 

        sheet1 = wb['Sheet1']

        for i in range(1, 1000): 
            cellA = 'A'+ str(i+1) 
            cellB = 'B'+ str(i+1) 
            cellA_value = sheet1[cellA].value 
            cellB_value = sheet1[cellB].value 

            if cellA_value == None or cellB_value == None: 
                break; 
            

            sf_type = get_object_or_404(ScreenFieldType, name=cellB_value)

            ScreenField.objects.create(
                page=page, 
                sf_type=sf_type, 
                name = cellA_value
                
            )


    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def delete_screen_field(request, id): 
    get_object_or_404(ScreenField, id=id).delete() 

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    

def download_excel_standard_file(request): 
    
    file = ExcelTemplate.objects.last().file 
    file_path = file.path 
    file_name= file.name 

    with open(file_path, 'rb') as f: 
        file_data = f.read() 

        response = HttpResponse(file_data, content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = f'attachment; filename="template.xlsx"'
    
    return response