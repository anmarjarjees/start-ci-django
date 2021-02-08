# Django imports the class "TestCase"
# this class is na extension of the Python standard library module called "Unit Tests"
# which provides us with many methods to assert various things about our code
from django.test import TestCase

# Create your tests here.

# starting by creating our class "TestDjango" which inherits the built-in "TestCase" class from Django


class TestDjango(TestCase):
    # Every test will be defined as a method that start with the word "test":
    # Like any method inside a class, has to have self as a parameter:
    # Remever that the keyword "self" in python is similar to the keyword "this" in JavaScript
    # "self" refers to our TestDjango class
    def test_this_thing_works(self):
        # now we can use the pre-built methods and functionality that are inherited from "TestCase":
        # using the built-in assert equal method to determine whether one equals zero:
        # First # self.assertEqual(1, 0)  # 1 is not equal to 0 => this test should fail
        # make it pass:
        self.assertEqual(1, 1)  # This test will pass

    # we should delete all the wrong tests (functions) in this file and create new ones
    def test_this_thing_works2(self):
        # now we can use the pre-built methods and functionality that are inherited from "TestCase":
        # using the built-in assert equal method to determine whether one equals zero:
        self.assertEqual(1, 0)  # 1 is not equal to 0 => this test should fail

    def test_this_thing_works3(self):
        # now we can use the pre-built methods and functionality that are inherited from "TestCase":
        # using the built-in assert equal method to determine whether one equals zero:
        self.assertEqual(1, )  # This test will have as syntax error

    def test_this_thing_works4(self):
        # now we can use the pre-built methods and functionality that are inherited from "TestCase":
        # using the built-in assert equal method to determine whether one equals zero:
        self.assertEqual(1, 4)  # 1 is not equal to 4 => this test should fail

# NOTE: To run our test => python3 manage.py test
# .FEF ==>  The first line in our result:
# -	. the dot for the first test that passed
# -	F for the second test that failed
# -	E for the third one that has error
# -	F for the fourth (last) one that failed

# You can try to correct the code by making it: assertEqual(1,1)
# And you will receive four dots: ....

# ******************************************************
# Please DON"T forget that we used this default tests.py file for learning,
# We will change this file name from the default name which is "tests.py" to our new custom name "test_views"
# Using custom names will:
#  help us to separate our testing logic in order to keep it organized and easy to manage
#  make our tests more independent of one another

# So this test is called "test_views" just for testing our views as the name indicats
