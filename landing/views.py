from django.shortcuts import render,redirect
# Create your views here.

def Main(request):
    return render(request,'landing/main.html')