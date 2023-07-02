from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request,"home.html")

def postUser(request):
    if request.method == 'POST':  # Use 'method' with lowercase letters
        name = request.POST.get("name")
        age = request.POST.get("age")
        # Process the name and age data here
        return HttpResponse("Hello, " + name + "! You are " + age + " years old.")
    elif request.method == 'GET':  # Use 'method' with lowercase letters
        return render(request, "index.html")
    else:
        return HttpResponse("Method not allowed")

