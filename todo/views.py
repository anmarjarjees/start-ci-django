# We need to import HttpResponse from the Django shortcuts
# We commented the "HTTPResponse" as we don't want this module after rendering html pages


from django.shortcuts import render # , HttpResponse

# Now to render the database contents in a template (html page)
# We need to import our class Item from .models files:
from .models import Item

# Create your views here.


# say_hello() function takes an http request from the user and return an http response
# def say_hello(request):
# return HttpResponse("Hello")

# we can also remove HttpResponse as we don't need it with rendering the full template
# render function takes two arguments:
# The HTTP request
# The template name as it's
# and return the rendered template:
# def get_todo_list(request):
# return render(request, 'todo/todo_list.html')

# The new get_todo_list view => dealing with the database:
def get_todo_list(request):
    # run a querty to get all the items from our database table "items"
    # and save the result into a python variable named "items"
    items = Item.objects.all()

    # Creating another variable "context" to be a dictionay with all the returned items infomraiton:
    context = {
        # first key "items" has the values of our items variable above
        'items': items
    }

    # now we can add/pass the "context" as a third argument to the render function:
    # to access the content in our todo_list.html template 
    return render(request, 'todo/todo_list.html', context)


# The new get_todo_list view => dealing with the database:
def add_item(request):
    return render(request, 'todo/add_item.html')