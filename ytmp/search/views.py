
import requests 
from django.shortcuts import redirect, render
from django.conf import settings
from django.http import HttpResponse
from .forms import ContactForm


def index(request):
    form = ContactForm()
    context = {'form': form}
    return render(request, 'search/index.html')

