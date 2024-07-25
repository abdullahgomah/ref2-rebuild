from django.shortcuts import render, get_object_or_404
from .models import * 

# Create your views here.

def main_interface(request): 
    context = { }
    return render(request, 'app_v2/main-interface.html', context)



def index(request): 

    projects = Project.objects.all() 

    if request.POST: 
        project_name = request.POST.get('project-name-input') 
        Project.objects.create(name=project_name)

    context = {
        'projects': projects,
    }
    return render(request, 'app_v2/index.html', context)


def project_details(request, id): 
    project = get_object_or_404(Project, id=id) 
    field_types = FieldType.objects.all() 

    if request.POST: 
        name = request.POST.get('field-name-input') 
        f_type = request.POST.get('field-type-select') 
        f_type = FieldType.objects.get(name=f_type) 

        field = Field.objects.create(
            project = project, 
            name = name, 
            f_type = f_type 
        )

        print(name) 
        print(f_type) 

    context = {
        'project': project, 
        'f_types': field_types, 
    } 
    return render(request, 'app_v2/project-details.html', context)