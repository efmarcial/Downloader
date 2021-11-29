
from django.db import models

class Contact(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.email

class imggal(models.Model):
    imgTitle = models.CharField(max_length=100)
    imgDsec = models.CharField(max_length=500)
    img = models.ImageField(upload_to = 'images/')