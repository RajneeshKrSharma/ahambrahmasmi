from rest_framework import serializers
from .models import ImageResource, SchedifyResource


class ImageResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageResource
        fields = '__all__'

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