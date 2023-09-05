#!/usr/bin/python3
"""a function to print your name"""


def say_my_name(first_name, last_name=""):
    """a function to print the first and last name

    first_name => the first name
    last_name => the last name
    """
    if isinstance(first_name, str) is not True:
        raise TypeError("first_name must be a string")
    elif isinstance(last_name, str) is not True:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
