from django.contrib import admin

# Register your models here.

from .models import image, preview_smoothie, Smoothie, Aguas, Snacks, page_descripton

admin.site.register(image)
admin.site.register(preview_smoothie)
admin.site.register(Smoothie)
admin.site.register(Snacks)
admin.site.register(Aguas)
admin.site.register(page_descripton)