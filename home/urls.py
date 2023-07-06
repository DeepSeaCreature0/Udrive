from django.urls import path
from . import views
from django.urls import reverse

urlpatterns = [
    path("", views.Home, name="Home"),
    # path("favourites/", views.favourites, name="favourites"),
    path("addFolder/", views.addFolder, name="addFolder"),
    path("addFolder/<int:parent_id>/", views.addFolder, name="add_subfolder"),
    path("logout/", views.Logout, name="Logout"),
    path("folder/<int:folderid>/", views.folder, name="folder"),
    path("uploadFile", views.uploadFile, name="uploadFile"),
    path("uploadFile/<int:parent_id>", views.uploadFile, name="uploadsubFile"),
    path(
        "toggleFavoriteFolder/<int:folder_id>/",
        views.toggleFavoriteFolder,
        name="toggleFavoriteFolder",
    ),
    path(
        "toggleFavoriteFile/<int:file_id>/",
        views.toggleFavoriteFile,
        name="toggleFavoriteFile",
    ),
    path("delete_folder/<int:folder_id>/", views.delete_folder, name="delete_folder"),
    path("delete_file/<int:file_id>/", views.delete_file, name="delete_file"),
    path("toggleRenameFolder/<int:folder_id>/",views.toggleRenameFolder,name="toggleRenameFolder"),
    path("toggleRenameFile/<int:file_id>/",views.toggleRenameFile,name="toggleRenameFile"),
    path('togglePublicFolder/<int:folder_id>/',views.togglePublicFolder,name="togglePublicFolder"),
    path('togglePublicFile/<int:file_id>/',views.togglePublicFile,name="togglePublicFile"),
]
