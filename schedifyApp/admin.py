from django.contrib import admin

from schedifyApp.models import ScheduleListAttachment, Config, WeatherStatusImages
from .models import SchedifyResource

@admin.register(ScheduleListAttachment)
class ScheduleListAttachmentsAdmin(admin.ModelAdmin):
    list_display = ["uniqueScheduleId", "file"]

@admin.register(Config)
class ConfigAdmin(admin.ModelAdmin):
    list_display = ["key", "value"]


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


@admin.register(WeatherStatusImages)
class WeatherStatusImagesAdmin(admin.ModelAdmin):
    list_display = ['id', 'url', 'status']
