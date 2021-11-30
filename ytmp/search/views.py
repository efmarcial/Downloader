
import requests 
from django.shortcuts import redirect, render
from django.conf import settings
from django.http import HttpResponse
from .forms import ContactForm

from .models import imggal


def index(request):
    
    resultsdisplay = imggal.objects.all()
    context = {
        'imggal' : resultsdisplay,
        'post' : 'post'
    }
    return render(request, 'search/index.html', {'imggal':resultsdisplay})

