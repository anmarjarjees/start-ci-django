# still need to import django.test from TestCase
from django.test import TestCase

# importing the ItemFrom from .froms:
from .forms import ItemForm

# Creating a new class "TestItemForm" that inherits all the TestCase form (including all its tests):


class TestItemForm(TestCase):

    # Test 1: Making sure that name field is required:
    # give our test a meaningful name:
    def test_item_name_is_required(self):
        # instantiating a form and it will be done without a name
        # to simulate that the user submits the form without name:
        form = ItemForm({'name': ''})

        # this form SHOULD NOT be valid (no name)!
        # so we will use assert false to ensure that this is the case "Form Should be invalid due to the empty name field":
        self.assertFalse(form.is_valid())

        # if the form is not valid we should sent a dictionary with the empty fields and their corsponding error messages
        # Being more specific by checking if the 'name' key is in the dictionary of form erros keys
        self.assertIn('name', form.errors.keys())

        # finally, using assert equal to check if the error message on the name field is required:
        # This string has to match exactly the error string in django by including also the period at the end
        # Also we are using the index of 0, because the form will return a list of errors on each field
        # To summarize, this verifies that the first item in that list is our string telling us the field is required
        self.assertEqual(form.errors['name'][0], 'This field is required.')

        # The step logic:
        # 1) Testing that the form is not valid:
        # self.assortFalse(form.is_valid())
        # 2) The error occured on the name filed:
        # self.assertIn('name', form.errors.key())
        # 3) The specific error message "This field is required" is expected that the name field is required after running this test:
        # self.assertEqual(form.error['name'][0], 'This field is required.')

    # Test 2: Making sure that done field is not required:
    # remember that the "done" field has a default value of "false" on the item model => that's why it shouldn't be a required field

    def test_done_field_is_not_required(self):
        # creating a form by sending only the name as a required field and ignoring the done status field as it's not required (not selected)
        form = ItemForm({'name': 'Test Todo Item'})
        self.assertTrue(form.is_valid())

    # Life-Case Scenario:
    # another developer might change the class "Item" by adding some helpful/utilities field(s) that we don't want to display for the user/client
    # the client should only see the name and done fields on the form
    # Here is the reason why we used metaclass which to insure only the fields we specified in the field list inside the metaclass will be displayed

    # Test 3: Making sure that only the name and done fields will be displayed (in case if there are others)
    def test_fields_are_explicit_in_form_metaclass(self):
        # instantiate an empty form:
        # Using assert equal to check whether for form.meta.fields attribute is equal to a list with name and "done" in it:
        form = ItemForm()
        self.assertEqual(form.Meta.fields, ['name', 'done'])
        # To summarize the test:
        # This will ensure that the fields "name" and "done" are defined explicitly,
        # If someone changes the item model by adding other extra field(s)
        # Our form will not display the information (extra fields) that we don't want to display

        # Notice that this will also protect against the fields being reordered!
        # It has to match the exact list: "name" field then "done" field
