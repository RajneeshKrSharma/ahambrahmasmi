from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import ImageResource, SchedifyResource

@admin.register(ImageResource)
class ImageResourceAdmin(admin.ModelAdmin):
    list_display = ['id', 'image_name', 'url', 'image_file', 'created_at', 'updated_at']
    search_fields = ['image_name']
    list_filter = ['created_at']


from django.contrib import admin
from .models import SchedifyResource


@admin.register(SchedifyResource)
class SchedifyResourceAdmin(admin.ModelAdmin):
    # Columns in the list page
    list_display = (
        "id",
        "url",
        "image_name",
        "image_file",
        "created_at",
        "updated_at",
    )

    # Fields shown in the detail (edit) page
    fields = (
        "url",
        "image_name",
        "image_file",
        "created_at",
        "updated_at",
    )

    # Make timestamps read-only
    readonly_fields = ("created_at", "updated_at")

    # Filters in the right sidebar
    list_filter = ("created_at", "updated_at")

    # Searchable fields
    search_fields = ("id", "url", "image_name")

    # Default ordering
    ordering = ("-created_at",)
