# We need to import HttpResponse from the Django shortcuts
# We commented the "HTTPResponse" as we don't want this module after rendering html pages

from django.shortcuts import render, redirect, get_object_or_404  # , HttpResponse

# Now to render the database contents in a template (html page)
# We need to import our class Item from .models files:
from .models import Item

# now to use the Django feature of form templating that we created inside the file "forms.py"
# we have to import our models "ItemForm" from ".forms" file "forms.py":
from .forms import ItemForm

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

# Below is our old first function using pure HTML form
# I renamed it to add_item_old as we will have the new add_item() function below it


def add_item_old(request):
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

# the new modified add_item() view after applying Django form template feature (from our file forms.py):


def add_item(request):
    # First, we need to check what type of request this is, GET or POST?
    # GET is the default option only for rendering a specific template (HTML page) as written at the end of this function
    # POST is what we have to use here for posting the usring input to our database
    # So if it's "POST" request, we will run the code in this if condition block:
    if request.method == 'POST':
        # The other new changes:
        # Instead of creating the items manually => name = request.POST.get('item_name')
        # We will let our new form from forms.py do it:
        # We can use a similar syntax as we did with creating the empty form
        # but here we will populate the form in Django with request.Post data:
        form = ItemForm(request.POST)
        # then calling is_valid() method in the form, and Django will automatically compare the data submitted in the post request
        # to the data required on the model and make sure everything matches up
        if form.is_valid():
            # now to save our item we need to use:
            form.save()

            # Then redirect to the "get_todo_list" template as before
            return redirect('get_todo_list')

    # After importing our model ItemForm [Created inside forms.py], we can create an instance of it
    form = ItemForm()

    # creating a context object variable to contains the empty form
    context = {
        'form': form
    }
    # Then we can return the context to the template in render function below:

    # If it's only a "GET" request (which is the default one), it will just redner the "add_item.html" page:
    # we changed it by adding "context" argument
    return render(request, 'todo/add_item.html', context)

# the view "edit_item()":
# This view will take the item_id paramater as it's required to grap that specific item from the database
# The value of this item_id will be attached to the "/edit" link


def edit_item(request, item_id):
    # We need to grap the selected item from the database based on its id value:
    # we can do it using a built-in Django shortcut method (function) called get_object_or_404
    # this short cut (method) will get an instance of the "Item" model with an ID equal to the item ID that was passed into the view via the URL
    # if the item is exist, the method will return it, otherwise it will return a 404 page
    # Notice that this method "get_object_or_404" has to be imported to this file (at the top)
    item = get_object_or_404(Item, id=item_id)

    # the same block of handeling the post request from "add_item"
    if request.method == 'POST':
        # changing the ItemForm by adding the instance:
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            # now to save our item we need to use:
            form.save()

            # Then redirect to the "get_todo_list" template as before
            return redirect('get_todo_list')

    # the same like add_item view, we will create an instance of our item:
    # NOTE:
    # To repopulate the form with the current item's details from the database
    # we can pass an instance argument to the form and fill it with the full information of the item that we got from the database in the first line
    form = ItemForm(instance=item)
    context = {
        'form': form
    }
    # this view returns a template named "edit_item.html"
    return render(request, 'todo/edit_item.html', context)
