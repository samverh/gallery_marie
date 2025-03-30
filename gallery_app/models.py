from django.db import models
from cloudinary.models import CloudinaryField

class Image(models.Model):
    title = models.CharField(max_length=255)
    image = CloudinaryField("image", null=True)  # This automatically uploads to Cloudinary
    # image = models.ImageField(upload_to='images')
    def __str__(self):
        return self.title

# class Image(models.Model):
#     title = models.CharField(max_length=70)
#     set = models.CharField(max_length=70, null=True, blank=True)
#     photo = models.ImageField(upload_to='images', null=True, blank=True)

# # class Image(models.Model):
# #     # image = models.FileField()
# #     photo = models.BinaryField(null=True)
# #     title = models.CharField(max_length=70)
# #     set = models.CharField(max_length=70, null=True, blank=True)

#     def __str__(self):
#         return self.title