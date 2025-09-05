from django.db import models

class ImageResource(models.Model):
    url = models.URLField(max_length=500, blank=True, null=True)
    image_name = models.CharField(max_length=255)
    image_file = models.ImageField(upload_to='images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    def __str__(self):
        return self.image_name