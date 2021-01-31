# By default, Djngo imports the models folder from django / db directory / inside the site-packages
# here is the link for Django github: https://github.com/django/django
# then you can follow this path: django/django/db/models/__init__.py
# inside the file __init__.py, you will see this line:
# from django.db.models.base import DEFERRED, Model  # isort:skip

from django.db import models

# Create your models here.

# Creating our class "Item"
# Django will convert the "Item" class to "items" table in the database!
# Any custom class we add to python, we have to use class inhertince to inhirit from python models as explained above
# below we are inherting from Django the base models.Model class:
# this is the basic concept of OOP [Please refer to my lecture about OOP in Python for more details]
class Item(models.Model):
    # we need to define the attributes (the fields):
    # plus adding some restrictions for each field

    # name field:
    # maximum 50 characters
    # null=False => to prevent created/inserting a new item without a name programmatically (the backend - srouce code)
    # blank=False => will make the field required on forms (the view)
    # With these two constraints, we can be sure the this field will never be empty by the user form or the python code or in the admin panel
    name = models.CharField(max_length=50, null=False, blank=False)

    # adding the same resitrictions for done field below and adding a defualt value of False:
    done = models.BooleanField(null=False, blank=False, default=False) 

    # By default all models that inherit this base model class will use its built-in string method to display their class name followed by the word object as a generic way to display them
    # To change this default returned string to something meaningful, we need to override this method: __str__(self)
    def __str__(self):
        # just return the name attribute (the name field of our current class Item)
        return self.name 