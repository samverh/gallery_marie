from django.contrib import admin

from .models import Image

class imageAdmin(admin.ModelAdmin):
    list_display = ("id", "image", "title")

admin.site.register(Image, imageAdmin)