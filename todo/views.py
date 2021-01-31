# We need to import HttpResponse from the Django shortcuts
from django.shortcuts import render, HttpResponse

# Create your views here.


# say_hello() function takes an http request from the user and return an http response
# def say_hello(request):
# return HttpResponse("Hello")

# we can also remove HttpResponse as we don't need it with rendering the full template
# render function takes two arguments:
# The HTTP request
# The template name as it's
# and return the rendered template:
def get_todo_list(request):
    return render(request, 'todo/todo_list.html')
