
import requests 
from django.shortcuts import redirect, render
from django.conf import settings
from django.http import HttpResponse
import os
from pathlib import Path
import os.path


def index(request):

    return render(request, 'search/index.html')

