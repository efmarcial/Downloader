
import requests 
from django.shortcuts import redirect, render
from django.conf import settings
from django.http import HttpResponse

from .models import image, menu, Contact


def index(request):

    if (request.method == 'POST'):
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact = Contact(name=name, email=email, message=message)
        contact.save()
    
    image_display = image.objects.all()
    menu_display = menu.objects.all()
    context = {
        'image' : image_display,
        'item' : menu_display
    }
    return render(request, 'search/index.html', context)

