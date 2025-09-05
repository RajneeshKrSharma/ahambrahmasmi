from rest_framework.views import APIView

from schedifyApp.models import SchedifyResource
from schedifyApp.serializers import SchedifyResourceSerializer
from .utils.helper import get_config_value

# Create your views here.
class SchedifyResourceView(APIView):
    def get(self, request):
        items = SchedifyResource.objects.all()
        serializer = SchedifyResourceSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status

from .models import ScheduleListAttachment
from .serializers import ScheduleListAttachmentUploadSerializer

import os
from django.conf import settings

class UploadScheduleAttachmentsView(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def get(self, request):
        uniqueScheduleId = request.query_params.get("uniqueScheduleId")
        if not uniqueScheduleId:
            return Response(
                {"error": "uniqueScheduleId is required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        attachments = ScheduleListAttachment.objects.filter(uniqueScheduleId=uniqueScheduleId)

        if not attachments.exists():
            return Response(
                {"message": "No attachments found for this schedule"},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = ScheduleListAttachmentUploadSerializer(attachments, many=True)
        return Response({"attachments": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        uniqueScheduleId = request.data.get("uniqueScheduleId")
        if not uniqueScheduleId:
            return Response(
                {"error": "uniqueScheduleId is required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if "files" not in request.FILES:
            return Response(
                {"error": "No files uploaded"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # 🔑 Fetch max size from config
        max_size_mb = float(get_config_value("MAX_ATTACHMENT_SIZE_MB", default=1))
        max_size = int(max_size_mb * 1024 * 1024)

        files = request.FILES.getlist("files")

        # ✅ पहले पुराने attachments हटा दो (DB + File system से)
        old_attachments = ScheduleListAttachment.objects.filter(uniqueScheduleId=uniqueScheduleId)
        for att in old_attachments:
            if att.file and os.path.isfile(att.file.path):
                os.remove(att.file.path)   # delete actual file
            att.delete()  # delete DB record

        uploaded_files = []

        for f in files:
            if f.size > max_size:
                file_size_kb = round(f.size / 1024, 2)
                file_size_mb = round(f.size / (1024 * 1024), 2)

                return Response(
                    {
                        "error": (
                            f"File '{f.name}' is too large "
                            f"({file_size_kb} KB ≈ {file_size_mb} MB). "
                            f"Maximum allowed size is {max_size_mb} MB."
                        )
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )

            attachment = ScheduleListAttachment.objects.create(
                uniqueScheduleId=uniqueScheduleId,
                file=f,
            )
            uploaded_files.append(attachment)

        serializer = ScheduleListAttachmentUploadSerializer(uploaded_files, many=True)
        return Response({"attachments": serializer.data}, status=status.HTTP_201_CREATED)
