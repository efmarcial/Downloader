
from django.db import models
from django.db.models.deletion import CASCADE

class Contact(models.Model):
  name = models.CharField(max_length=122)
  email = models.EmailField(max_length=120)
  message = models.TextField()

class image(models.Model):
    img = models.ImageField(upload_to = 'images/')


class menu(models.Model):

    title = models.CharField(max_length=50)
    discription = models.CharField(max_length=50)
    price = models.CharField(max_length=50)

class information(models.Model):
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
