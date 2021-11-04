from os import name
from re import UNICODE
from django.db import models

# Create your models here.

class File(models.Model):
    video_name = models.CharField(max_length=100)
    filepath = models.FileField(upload_to='files/', null=True, verbose_name='')

    def __str__(self) -> str:
        return self.video_name + ': ' + str(self.filepath)