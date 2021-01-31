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

# using get to do list:
from todo.views import get_todo_list

urlpatterns = [
    path('admin/', admin.site.urls),
    # Using path() function:
    # path('hello/', say_hello, name="hello")
    # replace the url with empty string to access the required view (function) directly - acting as a home page:
    path('', get_todo_list, name="get_todo_list")
]
