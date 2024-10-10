from django.shortcuts import render, get_object_or_404, redirect
from .models import * 
from urllib.parse import quote
from django.http import HttpResponseRedirect
from django.http import HttpResponse
import os 
from zipfile import ZipFile
from openpyxl import load_workbook

from base.models import Tool 

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
            ## generate css code 
            code.write('<!DOCTYPE html>\n')
            code.write('<html dir="rtl" lang="ar" >\n')
            code.write('<head>\n')
            code.write(f'<title>{page.name}</title>\n')
            code.write('<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.rtl.min.css" integrity="sha384-gXt9imSW0VcJVHezoNQsP+TNrjYXoGcrqBZJpry9zJt8PCQjobwmhMGaDHTASo9N" crossorigin="anonymous">')
            code.write('<style>\n') 

            for field in page.s_fields.all(): 
                code.write(f'#id{field.id} {{\n')
                code.write(f"\theight: {field.height};\n")
                code.write(f'\tcolor: {field.color};\n')
                

                code.write(f"\tfont-size: {field.font_size}px; \n")
                code.write(f'}}\n')
            # height
            # width 
            # color 
            # bgcolor 
            # bgurl 
            # padding
            # margin 
            # fontsize
            # fontweight 
            # fontfamily 

            code.write('</style>\n' )
            code.write('</head>\n')

            code.write('<body>\n')

            code.writelines("""
            <!--
            يوجد بعض النصائح الخاصة بعدة عناصر اكتبها لك هنا لتساعدك أثناء تخصيص صفحتك
            الأزار: الكلاس الافتراضي الموجود في الأزرار هو btn-primary

            يمكنك تغييره لعدة قيم أخرى حسب رغبتك 
            زر خطر: btn-danger 
            زر تحذير: btn-warning
            زر غامق: btn-dark 
            زر معلومات: btn-info 
            زر نجاح العملية: btn-success                 
            -->
            """)

            for field in page.s_fields.all(): 
                cmd = field.cmd 
                cmd = str(cmd)

                code.write("\t" + cmd) 
                code.write('\n')
            
            code.write('</body>\n')
            
            code.write('<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>')
            
            code.write("\n")
            
            code.write('<script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js" integrity="sha384-IQsoLXl5PILFhosVNubq5LC7Qb9DXgDA9i+tQ8Zj3iwWAwPtgFTxbJ8NT4GN1R8p" crossorigin="anonymous"></script>')
            
            code.write('\n')

            code.write('</html>')


    
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


def get_field_info(request): 
    if request.GET: 
        id = request.GET.get('id') 

        field = get_object_or_404(ScreenField, id=id) 

        sf_types = ScreenFieldType.objects.all() 

        context = {
            'field': field,
            'sf_types': sf_types, 
        }
        return render(request, 'v3/overlay-edit-screenfield.html', context)
    
    elif request.POST: 
        field_id__input = request.POST.get('field__ID') 
        field = get_object_or_404(ScreenField, id=field_id__input)

        field_name__input = request.POST.get('filed__name__input')
        
        field_type__input = request.POST.get('sf_type__input')
        field_type = get_object_or_404(ScreenFieldType, name=field_type__input)

        field_height_input = request.POST.get('field__height__input') 
        field_width_input = request.POST.get('field__width__input') 

        color_input = request.POST.get('color__input') 
        bgcolor_input = request.POST.get('bgcolor__input') 

        field_padding__input = request.POST.get('field_padding_input')

        field_margin__input = request.POST.get('field_margin_input') 

        field_fontsize__input = request.POST.get('font_size__input') 
        field_fontfamily__input = request.POST.get('font_family__input') 
        field_fontweight__input = request.POST.get('font_weight__input') 

        field.name = field_name__input 
        field.sf_type =field_type 
        field.height = field_height_input 
        field.width = field_width_input 
        field.color = color_input 
        field.bg_color = bgcolor_input 
        field.padding = field_padding__input 
        field.margin = field_margin__input 
        field.font_size = field_fontsize__input
        field.font_family = field_fontfamily__input 
        field.font_weight = field_fontweight__input

        field.save() 

        return redirect("v3:page-details", id=field.page.id)


def fields_branch_interface(request): 

    tools = Tool.objects.all() 


    context = {
        'tools': tools, 
    } 
    return render(request, 'v3/fields-branch-interface.html', context)


def single_tool_field_branch(request, id): 
    tool = get_object_or_404(Tool, id=id) 

    context = {
        'tool': tool,
        'fields': tool.fields.all() 
    }

    return render(request, 'v3/single_tool_field_branch.html', context)