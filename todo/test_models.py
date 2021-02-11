# Starting by importing TestCase first:
from django.test import TestCase

# Then importing our Item model as this test is all about our models, we only have this one:
from .models import Item

# Creating our new class "TestModel" that inherits from TestCase


class TestModel(TestCase):
    def test_done_default_to_false(self):
        # This will be a simple test by just creating an item with this name value:
        item = Item.objects.create(name='Test Todo Item')

        # Using assertFalse() to confirm that its done status is False by default:
        self.assertFalse(item.done)

# We can now run just this test file

# after checking the ceverage report we found that we also need to test the method [def __str__(self):]
# testing if this method does return the item name:
    def test_item_string_method_returns_name(self):
        # creating an item with a text (name's value) of "Test Todo Item"
        item = Item.objects.create(name='Test Todo Item')
        # using assertEqual() to confirm that this name is returned when we render this item as a string:
        self.assertEqual(str(item),'Test Todo Item')
