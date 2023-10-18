from django.db import models

# class Image(models.Model):
#     title = models.CharField(max_length=70)
#     set = models.CharField(max_length=70, null=True, blank=True)
#     photo = models.ImageField(upload_to='images')

class Image(models.Model):
    # image = models.FileField()
    photo = models.BinaryField(null=True)
    title = models.CharField(max_length=70)
    set = models.CharField(max_length=70, null=True, blank=True)