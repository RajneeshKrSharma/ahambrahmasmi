from django.urls import path
from .views import ImageResourceView

urlpatterns = [
    path('images', ImageResourceView.as_view(), name='image-resources'),
]