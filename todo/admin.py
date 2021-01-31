from django.contrib import admin

# from the current directories "models files" => import the "Item" class
from .models import Item

# Register your models here.
# using the register() function
admin.site.register(Item)