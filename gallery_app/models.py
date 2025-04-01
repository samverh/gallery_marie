from django.db import models
from cloudinary.models import CloudinaryField

class Image(models.Model):
    title = models.CharField(max_length=255)
    image = CloudinaryField("image", null=True)
    video = CloudinaryField("media", resource_type="auto", null=True)

    def __str__(self):
        return self.title
