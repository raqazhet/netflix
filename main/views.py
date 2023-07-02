from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request,"index.html")

def postUser(request):
    name = request.POST.get("name")  # Use 'POST' with uppercase letters
    age = request.POST.get("age")
    # Process the name data here
    return HttpResponse("Hello, " + name + "!" + age)