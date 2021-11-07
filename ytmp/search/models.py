from os import name
from re import UNICODE
from django.db import models
from django.db.models import manager

# Create your models here.



# Contact us model

class Feedback(models.Model):

    name = models.CharField(max_length=200, help_text="Name of the sender")
    email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.TextField(max_length=1000)
    data = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Feedback"

    def __str__(self) -> str:
        return self.name + '-' + self.email