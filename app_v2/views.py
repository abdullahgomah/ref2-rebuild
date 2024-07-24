from django.shortcuts import render
from .models import * 

# Create your views here.

def main_interface(request): 
    context = { }
    return render(request, 'app_v2/main-interface.html', context)