
import requests 
from django.shortcuts import redirect, render
from django.conf import settings
from django.http import HttpResponse

from .models import image, preview_smoothie, page_descripton


def index(request):
    
    image_display = image.objects.all()
    menu_display = preview_smoothie.objects.all()
    about = page_descripton.objects.all()
    context = {
        'image' : image_display,
        'item' : menu_display, 
        'about': about
    }
    return render(request, 'search/index.html', context)

