from os import name
from re import UNICODE
from django.db import models

# Create your models here.


class Video(models.Model):
    title = models.CharField(max_length=100)
    url_video = models.FileField(db_index=True, upload_to='media')
    