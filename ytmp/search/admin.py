from django.contrib import admin

# Register your models here.

from .models import image, menu, Contact, information

admin.site.register(image)
admin.site.register(menu)
admin.site.register(Contact)
admin.site.register(information)