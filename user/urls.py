from django.urls import path,include
from . import views

urlpatterns = [
    path("login", views.Login, name="Login"),
    path("signup", views.SignUp, name="SignUp"),
    path("home", include('home.urls')),
]