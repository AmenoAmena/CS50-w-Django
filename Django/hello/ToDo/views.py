from django.shortcuts import render

tasks = ["foo", "baz", "bar"]

def index(request):
    return render(request, "ToDo/index.html", {
        "tasks": tasks
    }) 
def add(request):
    return render(request,"ToDo/add.html" )