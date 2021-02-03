"""django_todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

# We need to import our Python function from views.py
# from todo.views import say_hello

# using get to do list and add item and edit_item view:
# Below is a long way:
# from todo.views import get_todo_list, add_item, edit_item, toggle_item
# instead of importing each view individually, we can just import the entire views file
from todo import views
# in such case we need to mention/write views before calling any function inside the views.py file, so all our urlspatterns has to be updated:
# we have to views. infront of all the views:

urlpatterns = [
    path('admin/', admin.site.urls),
    # Using path() function:
    # path('hello/', say_hello, name="hello")
    # replace the url with empty string to access the required view (function) directly - acting as a home page:
    path('', views.get_todo_list, name='get_todo_list'),
    path('add', views.add_item, name='add'),

    # adding a path with <item_id> the same as we did with my lecture for "Starting with Django Framework"
    # the angular bracket syntax: <item_id> is used with Django URLs
    # It is the mechanism by which the item ID makes its way from links or forms in our templates
    # through the URL and into the view which expects it as a parameter
    path('edit/<item_id>', views.edit_item, name='edit'),

    # the same parameters like "edit"
    path('toggle/<item_id>', views.toggle_item, name='toggle'),
    path('delete/<item_id>', views.delete_item, name='delete')
]
