from django.db import models
import uuid
import os

# Create your models here.
class Folder(models.Model):
    """Folder objects"""
    uid = models.UUIDField(primary_key=True, editable=False, default=uuid4.uuid)
    created_at = models.DateField(auto_now=True)

def get_upload_path(instance, filename):
    return os.path.join(str(instance.folder.uid), filename)

class Files(models.Model):
    """Files objects"""
    folder = models.ForeignKey(
        Folder,
        on_delete=models.CASCADE
    )
    file = models.FileField(upload_to=get_upload_path)
    created_at = models.DateField(auto_now=True)