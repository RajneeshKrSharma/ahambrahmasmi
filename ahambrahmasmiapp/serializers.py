from rest_framework import serializers
from .models import ImageResource


class ImageResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageResource
        fields = '__all__'