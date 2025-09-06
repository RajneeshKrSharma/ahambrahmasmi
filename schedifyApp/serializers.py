from rest_framework import serializers

from schedifyApp.models import SchedifyResource, ScheduleListAttachment, WeatherStatusImage


class SchedifyResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchedifyResource
        fields = [
            "id",
            "url",
            "image_name",
            "image_file",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at", "image_name"]


class ScheduleListAttachmentUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScheduleListAttachment
        fields = ['file']

    def to_representation(self, instance):
        return instance.file.url

class WeatherStatusImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherStatusImage
        fields = '__all__'