from django.db import models

class Image(models.Model):
    title = models.CharField(max_length=20)
    set = models.CharField(max_length=20, null=True, blank=True)
    photo = models.ImageField(upload_to='images')