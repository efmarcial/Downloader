from os import name
from re import UNICODE
from django.db import models
from django.core.files.storage import FileSystemStorage


# Create your models here.

fs = FileSystemStorage(location='/media/videos')


# Contact us model

class upload(models.Model):
    video =models.FileField(upload_to='media')