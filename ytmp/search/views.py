
import requests 
from django.shortcuts import redirect, render
from django.conf import settings
from django.http import HttpResponse

from .models import image


def index(request):
    
    resultsdisplay = image.objects.all()
    context = {
        'image' : resultsdisplay,
        'post' : 'post'
    }
    return render(request, 'search/index.html', {'image':resultsdisplay})

