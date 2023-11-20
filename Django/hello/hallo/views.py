from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,"hallo/index.html")
def arda(request):
    return HttpResponse("Hallo,arda")
def david(request):
    return HttpResponse("Hello,David")
def greet(request,name):
    return render(request,"hallo/greet.html",{
        "name": name.capitalize()
    })
