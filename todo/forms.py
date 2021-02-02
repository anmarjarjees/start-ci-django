# importing forms from Django to use some of the built-in form functionality of Django:
from django import forms

# Then importing our Item model (Class Item):
from .models import Item

# The same logic as we have done with our Item model (class Item),
# Our form will be a class that inherites a built-in Django class to give it some basic functionality:
# Let's name it "ItemForm" and it inherits all the functionality forms.ModelForm


class ItemForm(forms.ModelForm):
    # The next step, we need to tell the form which model it's going to be assoiciated with,
    # We need to provide an inner class called "Meta"
    # this class will just give our form some information about itself, just like meta tag for our HTML page
    class Meta:
        # define our Model which is "Item" model
        model = Item
        # identify the fields that we want to display from model which are 'name' and 'done' fields:
        # we define them as list:
        fields = ['name', 'done']


# To summerize, the idea of creating this forms.py file in django is giving us the option
# to let Django render the from as a template variable in our HTML page (by passing it to the render function)
# instead of creating the form elements by ourselves using HTML coding and applying the validations
