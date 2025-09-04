from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ImageResource, SchedifyResource
from .serializers import ImageResourceSerializer, SchedifyResourceSerializer


class ImageResourceView(APIView):
    def get(self, request):
        items = ImageResource.objects.all()
        serializer = ImageResourceSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ImageResourceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SchedifyResourceView(APIView):
    def get(self, request):
        items = SchedifyResource.objects.all()
        serializer = SchedifyResourceSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
