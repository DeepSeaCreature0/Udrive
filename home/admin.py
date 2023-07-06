from django.contrib import admin
from .models import Folder,File
# Register your models here.

@admin.register(Folder)
class Adminfolder(admin.ModelAdmin):
    list_display =('foldername','folderuser','created_at','parent_directory','favouriteFolder')

@admin.register(File)
class Adminfile(admin.ModelAdmin):
    list_display=('filename','fileuser','created_at','file_type','file_directory','favouriteFile')
