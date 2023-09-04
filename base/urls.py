from django.urls import path
from base import views

urlpatterns = [
    path('', views.HandleFileUpload.as_view(), name='file-upload'),
]
