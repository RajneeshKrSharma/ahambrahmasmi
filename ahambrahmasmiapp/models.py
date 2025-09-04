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

import os
from django.db import models


class SchedifyResource(models.Model):
    url = models.URLField(max_length=500, blank=True, null=True)
    image_name = models.CharField(max_length=255, blank=True)  # make blank=True so it can be auto-filled
    image_file = models.ImageField(upload_to='images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    def save(self, *args, **kwargs):
        # Call parent save first if instance doesn't have id yet (needed for filename_id)
        is_new = self.pk is None
        super().save(*args, **kwargs)

        if not self.image_name and self.image_file:
            base, ext = os.path.splitext(os.path.basename(self.image_file.name))
            self.image_name = f"{base}_{self.id}{ext}"  # e.g. xyz_15.png
            # Save again only if image_name was updated
            super().save(update_fields=["image_name"])

    def __str__(self):
        return self.image_name or "Unnamed Resource"

