from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import ImageResource

@admin.register(ImageResource)
class ImageResourceAdmin(admin.ModelAdmin):
    list_display = ['id', 'image_name', 'url', 'image_file', 'created_at', 'updated_at']
    search_fields = ['image_name']
    list_filter = ['created_at']