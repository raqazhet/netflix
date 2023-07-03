from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseBadRequest
from .models import User

# Create your views here.


def home(request):
    return render(request,"home.html")

def postUser(request):
    if request.method == 'POST':  # Use 'method' with lowercase letters
        user =User()
        user.name = request.POST.get("name")
        try:
            user.age = int(request.POST.get("age"))
            if user.age <10 or user.age>100:
                return HttpResponseBadRequest("invalid data")
        except ValueError:
            return HttpResponseBadRequest("Invalid age value")
        user.save()
        # Process the name and age data here
        return HttpResponse("Hello, " + user.name + "! You are " + str(user.age) + " years old.")
    elif request.method == 'GET':  # Use 'method' with lowercase letters
        return render(request, "index.html")
    else:
        return HttpResponse("Method not allowed")

