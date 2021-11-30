
from django.db import models
from django.db.models.deletion import CASCADE



class image(models.Model):
    tilte = models.CharField(max_length=100)
    desc = models.CharField(max_length=500)
    img = models.ImageField(upload_to = 'images/')


class Smoothie(models.Model):

    title = models.CharField(max_length=50)
    discription = models.CharField(max_length=50)
    price = models.CharField(max_length=50)

class Aguas(models.Model):

    title = models.CharField(max_length=50)
    discription = models.CharField(max_length=50)
    price = models.CharField(max_length=50)

class Snacks(models.Model):

    title = models.CharField(max_length=50)
    discription = models.CharField(max_length=50)
    price = models.CharField(max_length=50)


class preview_smoothie(models.Model):

    title = models.CharField(max_length=50)
    discription = models.CharField(max_length=50)
    price = models.CharField(max_length=50)


class page_descripton(models.Model):

    dicription = models.CharField(max_length=500)
