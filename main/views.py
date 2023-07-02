from django.shortcuts import render
from django.http import HttpResponse
from .models import User

# Create your views here.


def home(request):
    return render(request,"home.html")

def postUser(request):
    if request.method == 'POST':  # Use 'method' with lowercase letters
        user =User()
        user.name = request.POST.get("name")
        user.age = request.POST.get("age")
        user.save()
        # Process the name and age data here
        return HttpResponse("Hello, " + user.name + "! You are " + user.age + " years old.")
    elif request.method == 'GET':  # Use 'method' with lowercase letters
        return render(request, "index.html")
    else:
        return HttpResponse("Method not allowed")

