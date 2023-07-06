from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def Login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if username and password:
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("Home")
            else:
                messages.error(request, "Invalid username or password.")
                return redirect("Login")
    return render(request, "user/login.html")


def SignUp(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        password = request.POST.get("password")
        cpassword = request.POST.get("cpassword")
        
        if username and email and fname and lname and password and cpassword:
            if password == cpassword:
                if User.objects.filter(username=username).exists():
                    messages.error(request,"Username already taken")
                    return redirect("SignUp")
                elif User.objects.filter(email=email).exists():
                    messages.error(request,"Email already taken")
                    return redirect("SignUp")
                else:
                    user = User.objects.create_user(
                        username=username,
                        email=email,
                        password=password,
                        first_name=fname,
                        last_name=lname,
                    )
                if user:
                    return redirect("Login")
            else:
                messages.error(request, "Password does not match")
                return redirect("SignUp")

    return render(request, "user/signup.html")