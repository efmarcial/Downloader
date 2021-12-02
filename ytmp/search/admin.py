from django.contrib import admin

# Register your models here.

from .models import Image, Menu, Contact, Shop_Information

admin.site.register(Image)
admin.site.register(Menu)
admin.site.register(Contact)
admin.site.register(Shop_Information)