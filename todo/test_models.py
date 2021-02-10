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
