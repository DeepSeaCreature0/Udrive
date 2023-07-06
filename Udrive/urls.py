"""
URL configuration for Udrive project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from home import views as home_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("landing.urls")),
    path("home/", include("home.urls")),
    path("", include("user.urls")),
    path("favourites/", home_views.favourites, name="favourites"),
    path("profile/", home_views.Profile, name="profile"),
    path("profile_update/", home_views.updateProfile, name="profile_update"),
    path("folder/<int:folder_id>/download/", home_views.download_folder, name="download_folder"),
    path("folder/<int:folder_id>/<int:user_id>/download/", home_views.download_shared_folder, name="download_shared_folder"),
    path('download/file/<int:file_id>/', home_views.download_file, name='download_file'),
    path('download/file/<int:file_id>/<int:user_id>/', home_views.download_shared_file, name='download_shared_file'),
    path('allusers/',home_views.allusers,name="allusers"),
    path('allusers/sharedview/<int:user_id>/',home_views.sharedview,name="sharedview"),
    path("sharedfolder/<int:folderid>/<int:user_id>/", home_views.sharedfolder, name="sharedfolder"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
