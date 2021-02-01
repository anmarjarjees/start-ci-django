# We need to import HttpResponse from the Django shortcuts
# We commented the "HTTPResponse" as we don't want this module after rendering html pages


from django.shortcuts import render, redirect  # , HttpResponse

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
# so "/add" URL will trigger this view (function)


def add_item(request):
    # First, we need to check what type of request this is, GET or POST?
    # GET is the default option only for rendering a specific template (HTML page) as written at the end of this function
    # POST is what we have to use here for posting the usring input to our database
    # So if it's "POST" request, we will run the code in this if condition block:
    if request.method == 'POST':
        # We need to set two variables for name and done:
        # using get method with the value of "name" attribute that we specified in our HTML input form element: name="item_name"
        name = request.POST.get('item_name')
        # The checkbox is different as it's just a boolean value in our Database
        # So we have the check if the POSTED data has a "done" property in it
        # And we can do it by checking whether "done" is in request.post:
        done = 'done' in request.POST

        # Now we have the two required info to create a new item from our class Item
        # We already imported our Item model at the top
        # we will use the same concept as "Item.objects.all()" but this time we need to create an item not reading it:
        Item.objects.create(name=name, done=done)

        # Returning a redirect back to the view (function) "get_todo_list()" to render template/html page "todo_list.html"
        # Notice that we have now to import "redirect" from django.shortcuts at the top
        return redirect('get_todo_list')

    # If it's only a "GET" request (which is the default one), it will just redner the "add_item.html" page:
    return render(request, 'todo/add_item.html')
