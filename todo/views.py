# We need to import HttpResponse from the Django shortcuts
from django.shortcuts import render, HttpResponse

# Create your views here.


# say_hello() function takes an http request from the user and return an http response
def say_hello(request):
    return HttpResponse("Hello")
