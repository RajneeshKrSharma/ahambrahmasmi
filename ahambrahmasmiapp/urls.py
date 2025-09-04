from django.urls import path
from .views import ImageResourceView, SchedifyResourceView

urlpatterns = [
    path('images', ImageResourceView.as_view(), name='image-resources'),
    path('schedify-resource', SchedifyResourceView.as_view(), name='schedify-resources'),
]