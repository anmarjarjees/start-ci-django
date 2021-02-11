from django.test import TestCase
# We need to import our Item model to run the CRUD operations
from .models import Item

# Create your tests here.

# Task: Testing The Views:
# We just want to test that:
# 1) our views return a successful HTTP response with the proper template
# 2) our views and adding/toggling/deleting items


class TestViews(TestCase):
    # We will run 6 tests:

    # Test 1: Getting the "todo_list" which is the home page:
    def test_get_todo_list(self):
        # First Task: Test the HTTP responses of the views,
        # We can use a built-in HTTP client that comes with Django Testing framework
        # using self.client.get() method and assign the result to variable "response"
        # passing the the url "/" to refer to the home url address to get the home page
        response = self.client.get('/')
        # based on our status code table that we covered previously
        # We have 6 common HTTP Status Codes
        # The code "200" is for: Standard response for successful HTTP requests
        # so we will use assertEqual() to confirm that the response code is equal to 200
        self.assertEqual(response.status_code, 200)

        # Second Task: Confirm that view uses the correct template
        # we can use assertTemplateUsed() to specify the expected template to be used in the response:
        self.assertTemplateUsed(response, 'todo/todo_list.html')

    # Test 2: Getting the "adding_item" page:
    def test_get_add_item_page(self):
        # The same logic for the "todo_list" template:

        # Just changing the url value:
        response = self.client.get('/add')
        self.assertEqual(response.status_code, 200)

        # and change the template that we expected to use:
        self.assertTemplateUsed(response, 'todo/add_item.html')

    # Test 3: Getting the "editing_item" page:
    def test_get_edit_item_page(self):
        # Just changing the url value with adding the item_id:

        # NOTE: We can just pass a static number of "item_id" like 99 or 1,2
        # if the number (the item_id) exists in our database => the test will pass otherwise it will fail
        # Example: response = self.client.get('/edit/99')
        # For better test, we will use the CRUD operations Django test
        # With CRUD we need to import our model (class Item) and that's what we have done above

        # creating an item to be used in this test:
        item = Item.objects.create(name='Test Todo Item')

        # now we can pass the "item.id" variable below using Python f string:
        response = self.client.get(f'/edit/{item.id}')
        self.assertEqual(response.status_code, 200)

        # and change the template that we expected to use:
        self.assertTemplateUsed(response, 'todo/edit_item.html')

        # The last 3 tests below is for checking if we are able to:
        # - create item
        # - update item
        # - delete item

    # Test 4: Testing that we can add an item:
    def test_can_add_item(self):
        # To test the create operation, we can set the response to client.post on the "add" url:
        # Give a value for the item's name as if we've just submitted the item form
        response = self.client.post('/add', {'name': 'Test Added Item'})

        # If the item is addedd successfully, The view should redirect back to the home page
        # using assert to redirect the user to the home page:
        self.assertRedirects(response, '/')

    # Test 5: Testing that we can delete an item:
    def test_can_delete_item(self):
        # creating an item to be used in this test:
        item = Item.objects.create(name='Test Todo Item')

        # now we can pass the "item" variable below using Python f string,
        # Using the same syntax as with edit, but this time for delete url:
        response = self.client.get(f'/delete/{item.id}')
        # After deleting the item, the view should redirect us to the home page:
        self.assertRedirects(response, '/')

        # To make sure that the item was deleted successfully,
        # We will try to get it from the database:
        # using filter() and passing the item's id
        existing_item = Item.objects.filter(id=item.id)
        # now we can assert if the item's length is zero (no value-empty) which means not exists
        self.assertEqual(len(existing_item), 0)

    # Test 6: Testing that we can toggle an item:
    def test_can_toggle_item(self):
        # The first 3 lines almost the same as deleting an item:
        # Just by adding "status" value of "True" for "done" field:
        item = Item.objects.create(name='Test Todo Item', done=True)

        # Using the same syntax as with delete, but this time for toggle url also on his id value:
        response = self.client.get(f'/toggle/{item.id}')
        # After toggling the item, the view should redirect us to the home page:
        self.assertRedirects(response, '/')
        # getting the updated item form the database based on its id value:
        updated_item = Item.objects.get(id=item.id)
        # now we can assertFalse to check its done status:
        self.assertFalse(updated_item.done)

    # adding another test for "can edit an item":
    def test_can_edit_item(self):
        # like toggling an item, we will also create a new item (no need for done status):
        item = Item.objects.create(name='Test Todo Item')

        # to post the updated name:
        # Using the same syntax as with edit, but this time for "post()" instead of "get()":
        # now we can pass the "item.id" plus the "name" variable below using Python f string:
        response = self.client.post(
            f'/edit/{item.id}', {'name': 'Updated Name'})
        # then the same code as toggling, getting the updated item:
        # After editing the item, the view should redirect us to the home page:
        self.assertRedirects(response, '/')
        # getting the updated item form the database based on its id value:
        updated_item = Item.objects.get(id=item.id)
        # finally, we can test that the updated items name is equal to updated name using    assertEqual():
        self.assertEqual(updated_item.name, 'Updated Name')
