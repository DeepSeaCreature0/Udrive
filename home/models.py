from django.db import models
from django.contrib.auth.models import User
import os


# Create your models here.
class Folder(models.Model):
    foldername = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    folderuser = models.ForeignKey(User, on_delete=models.CASCADE)
    parent_directory = models.ForeignKey(
        "self", null=True, on_delete=models.CASCADE, blank=True
    )
    favouriteFolder = models.BooleanField(default=False)
    publicFolder=models.BooleanField(default=False)

    def __str__(self):
        return self.foldername


class File(models.Model):
    filename = models.CharField(max_length=200,default="")
    created_at = models.DateTimeField(auto_now_add=True)
    fileuser = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to="Files")
    file_directory = models.ForeignKey(
        Folder, null=True, on_delete=models.CASCADE, blank=True
    )
    favouriteFile = models.BooleanField(default=False)
    file_type = models.CharField(max_length=50, blank=True)
    split_value = models.CharField(max_length=200, default="okmybad")
    publicFile=models.BooleanField(default=False)

    def __str__(self):
        return self.filename
    
    def name(self):
        return os.path.basename(self.file.name)
