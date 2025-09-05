from django.urls import path
from .views import SchedifyResourceView, UploadScheduleAttachmentsView

urlpatterns = [
    path('schedify-resource', SchedifyResourceView.as_view(), name='schedify-resources'),
    path('schedule-items/upload-attachments', UploadScheduleAttachmentsView.as_view(), name='upload-attachments'),
]