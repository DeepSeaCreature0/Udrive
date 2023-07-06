# Create your views here.
from multiprocessing import context
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.files.base import ContentFile
from Udrive.settings import BASE_DIR
from .models import Folder, File
from django.urls import reverse
from django.conf import settings
import os
import zipfile
import shutil
from django.contrib import messages
import zipfile

@login_required(login_url="Login")
def Home(request):
    folder = Folder.objects.filter(folderuser=request.user, parent_directory=None)
    file = File.objects.filter(fileuser=request.user, file_directory=None)
    context = {
        "folder": folder,
        "title": "Home",
        "parent_id": None,
        "files": file,
        "title": "Home",
    }
    return render(request, "home/folder.html", context)


def favourites(request):
    favourite_folders = Folder.objects.filter(
        folderuser=request.user, favouriteFolder=True
    )
    favourite_files = File.objects.filter(fileuser=request.user, favouriteFile=True)
    context = {
        "folder": favourite_folders,
        "files": favourite_files,
        "title": "Favourite",
    }
    return render(request, "home/favourite.html", context)


def Logout(request):
    logout(request)
    return redirect("Login")


def addFolder(request, parent_id=None):
    parent_directory = None

    if parent_id:
        try:
            parent_directory = Folder.objects.get(id=parent_id, folderuser=request.user)
        except Folder.DoesNotExist:
            pass

    if request.method == "POST":
        foldername = request.POST.get("foldername")
        folder = Folder(
            foldername=foldername,
            folderuser=request.user,
            parent_directory=parent_directory,
        )
        folder.save()
    
    return redirect(request.META.get("HTTP_REFERER"))



def folder(request, folderid=1):
    if request.user.is_authenticated:
        folder = Folder.objects.filter(
            folderuser=request.user, parent_directory=folderid
        )
        parent = Folder.objects.get(id=folderid)
        title = parent.foldername
        file = File.objects.filter(fileuser=request.user, file_directory=folderid)
        context = {
            "folder": folder,
            "title": title,
            "parent_id": folderid,
            "files": file,
        }
        return render(request, "home/folder.html", context)
    else:
        return redirect("Login")


def uploadFile(request, parent_id=None):
    parent_directory = None

    if parent_id:
        try:
            parent_directory = Folder.objects.get(id=parent_id, folderuser=request.user)
        except Folder.DoesNotExist:
            pass

    if request.method == "POST":
        file_add = request.FILES.get("file")
        filename = file_add.name
        split_value = (
            "file" + "".join(letter for letter in filename if letter.isalnum())[:5]
        )

        fileadd = File(
            filename=filename,
            fileuser=request.user,
            file=file_add,
            file_directory=parent_directory,
            file_type=typefunction(filename),
            split_value=split_value,
        )
        fileadd.save()
        
    return redirect(request.META.get("HTTP_REFERER"))

def typefunction(filename):
    file_extension = filename.split(".")[-1].lower()
    file_type=""
    image = ["apng", "avif", "gif", "jpeg", "png", "svg", "webp", "jpg"]
    video = ["mp4", "mov", "avi", "wmv", "avchd", "webm", "flv", "mkv"]

    if file_extension in image:
        file_type = "Image"
    elif file_extension in video:
        file_type = "Video"
    elif file_extension == "pdf":
        file_type = "PDF"
    else:
        file_type = "Unknown"

    return file_type


def toggleFavoriteFolder(request, folder_id):
    folder = get_object_or_404(Folder, id=folder_id, folderuser=request.user)
    folder.favouriteFolder = not folder.favouriteFolder
    folder.save()
    return redirect(request.META.get("HTTP_REFERER"))


def toggleRenameFolder(request, folder_id):
    if request.method == 'POST':
        newname=request.POST.get('newname')
        folder = get_object_or_404(Folder, id=folder_id, folderuser=request.user)
        folder.foldername = newname
        folder.save()
    return redirect(request.META.get("HTTP_REFERER"))


def toggleFavoriteFile(request, file_id):
    file = get_object_or_404(File, id=file_id, fileuser=request.user)
    file.favouriteFile = not file.favouriteFile
    file.save()
    return redirect(request.META.get("HTTP_REFERER"))


def toggleRenameFile(request, file_id):
    if request.method == 'POST':
        newname=request.POST.get('newname')
        file = get_object_or_404(File, id=file_id, fileuser=request.user)
        file.filename = newname
        file.save()
    return redirect(request.META.get("HTTP_REFERER"))


def delete_folder(request, folder_id):
    folder = get_object_or_404(Folder, id=folder_id, folderuser=request.user)
    parent_id = folder.parent_directory_id
    folder.delete()
    if parent_id is None:
        return redirect("Home")
    else:
        return redirect(reverse("folder", kwargs={"folderid": parent_id}))


def delete_file(request, file_id):
    file = get_object_or_404(File, id=file_id, fileuser=request.user)
    parent_id = file.file_directory_id
    file.delete()
    if parent_id is None:
        return redirect("Home")
    else:
        return redirect(reverse("folder", kwargs={"folderid": parent_id}))
    
def Profile(request):
    user=request.user
    context={
        "user":user,
    }
    return render(request,"home/profile.html",context)

def updateProfile(request):
    if request.method == "POST":
        newusername=request.POST.get("username")
        newfname=request.POST.get("fname")
        newlname=request.POST.get("lname")
        newemail=request.POST.get("email")
        newpwd=request.POST.get("password")
        newcpwd=request.POST.get("cpassword")
        newphoto=request.FILES.get("p_img")

        user=request.user
        profile=user.profile
        change_in_password=False
        if newusername!=user.username:
            if User.objects.filter(username=newusername).exists():
                messages.error(request,"Username already taken")
                return redirect(request.META.get("HTTP_REFERER"))
            else:
                user.username=newusername
        if newfname!=user.first_name:
            user.first_name=newfname
        if newlname!=user.last_name:
            user.last_name=newlname
        if newemail!=user.email:
            if User.objects.filter(email=newemail).exists():
                messages.error(request,"Email already taken")
                return redirect(request.META.get("HTTP_REFERER"))
            else:
                user.email=newemail
        if newpwd and newcpwd:
            if newpwd != newcpwd:
                messages.error(request,"Password does not match")
                return redirect(request.META.get("HTTP_REFERER"))
            else:
                user.set_password(newpwd)
                change_in_password=True
        if newphoto:
            pname=newphoto.name
            file_extension = pname.split(".")[-1].lower()
            imagelist = ["apng", "avif", "gif", "jpeg", "png", "svg", "webp", "jpg"]
            if file_extension not in imagelist:
                messages.error(request,"Image not supported")
            else:
                profile.image=newphoto

        user.save()
        profile.save()
    
    if change_in_password:
        return redirect('Login')
    else:
        return redirect('profile')


def download_folder(request, folder_id):

    folder = get_object_or_404(Folder, id=folder_id, folderuser=request.user)
    zip_filename = f"{folder.foldername}.zip"
    temp_directory = os.path.join(settings.MEDIA_ROOT, "temp")

    if not os.path.exists(temp_directory):
        os.makedirs(temp_directory)

    zip_file_path = os.path.join(temp_directory, zip_filename)
    with zipfile.ZipFile(zip_file_path, "w") as zip_file:
        add_folder_to_zip(zip_file, folder)

    with open(zip_file_path, "rb") as zip_file:
        response = HttpResponse(zip_file.read())
        response["Content-Disposition"] = f"attachment; filename={zip_filename}"
        response["Content-Type"] = "application/zip"

    shutil.rmtree(temp_directory)

    return response

def download_shared_folder(request, folder_id,user_id):
    user=User.objects.get(id=user_id)
    folder = get_object_or_404(Folder, id=folder_id, folderuser=user)
    zip_filename = f"{folder.foldername}.zip"
    temp_directory = os.path.join(settings.MEDIA_ROOT, "temp")

    if not os.path.exists(temp_directory):
        os.makedirs(temp_directory)

    zip_file_path = os.path.join(temp_directory, zip_filename)
    with zipfile.ZipFile(zip_file_path, "w") as zip_file:
        add_folder_to_zip(zip_file, folder)

    with open(zip_file_path, "rb") as zip_file:
        response = HttpResponse(zip_file.read())
        response["Content-Disposition"] = f"attachment; filename={zip_filename}"
        response["Content-Type"] = "application/zip"

    shutil.rmtree(temp_directory)

    return response

def add_folder_to_zip(zip_file, folder, subfolder_path=""):
    files = File.objects.filter(file_directory=folder)
    for file in files:
        file_path = file.file.path
        parent_folder = folder.foldername
        zip_file.write(file_path, os.path.join(parent_folder, subfolder_path, file.filename))

    subfolders = Folder.objects.filter(parent_directory=folder)
    for subfolder in subfolders:
        updated_subfolder_path = os.path.join(subfolder_path, subfolder.foldername)
        add_folder_to_zip(zip_file, subfolder, updated_subfolder_path)


def download_file(request, file_id):
    file = get_object_or_404(File, id=file_id, fileuser=request.user)
    with open(file.file.path, "rb") as file_data:
        response = HttpResponse(file_data, content_type="application/octet-stream")
        response["Content-Disposition"] = f"attachment; filename={file.filename}"
    return response

def download_shared_file(request, file_id,user_id):
    user=User.objects.get(id=user_id)
    file = get_object_or_404(File, id=file_id, fileuser=user)
    with open(file.file.path, "rb") as file_data:
        response = HttpResponse(file_data, content_type="application/octet-stream")
        response["Content-Disposition"] = f"attachment; filename={file.filename}"
    return response
    
def togglePublicFolder(request,folder_id):
    folder=get_object_or_404(Folder,id=folder_id,folderuser=request.user)
    folder.publicFolder = not folder.publicFolder
    folder.save()
    return redirect(request.META.get("HTTP_REFERER"))

def togglePublicFile(request,file_id):
    file=get_object_or_404(File,id=file_id,fileuser=request.user)
    file.publicFile = not file.publicFile
    file.save()
    return redirect(request.META.get("HTTP_REFERER"))

def allusers(request):
    users=User.objects.all()
    context={
        "users":users,
        "title":"All Users"
    }
    if request.method=='POST':
        name=request.POST.get('searchInput')
        name=name.lower()
        filterusers=[]

        for user in users:
            if name in user.username:
                filterusers.append(user)
        context={
            "users":filterusers,
            "title":"Search result",
        }

        return render(request,'home/allusers.html',context)

    return render(request,'home/allusers.html',context)

def sharedview(request,user_id):
    user=User.objects.get(id=user_id)

    folder=Folder.objects.filter(folderuser=user)
    file=File.objects.filter(fileuser=user)
    
    publicFolders=[]
    publicFiles=[]

    for i in folder:
        if i.publicFolder:
            publicFolders.append(i)

    for i in file:
        if i.publicFile:
            publicFiles.append(i)

    context={
        "folder":publicFolders,
        "files":publicFiles,
        "title":"Shared Files",
        "user_id":user.id,
    }
    return render(request,'home/shared.html',context)

def sharedfolder(request, folderid=1,user_id=1):
    if request.user.is_authenticated:
        user=User.objects.get(id=user_id)
        folder = Folder.objects.filter(
            folderuser=user, parent_directory=folderid
        )
        parent = Folder.objects.get(id=folderid)
        title = "Shared "+parent.foldername
        file = File.objects.filter(fileuser=user, file_directory=folderid)
        
        context = {
            "folder": folder,
            "title": title,
            "parent_id": folderid,
            "files": file,
            "user_id":user.id,
        }
        return render(request, "home/shared.html", context)
    else:
        return redirect("Login")
  