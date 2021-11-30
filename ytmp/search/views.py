
import requests 
from django.shortcuts import redirect, render
from django.conf import settings
from django.http import HttpResponse

from .models import Image


def index(request):
    
    resultsdisplay = Image.objects.all()
    context = {
        'Image' : resultsdisplay,
        'post' : 'post'
    }
    return render(request, 'search/index.html', {'Images':resultsdisplay})

