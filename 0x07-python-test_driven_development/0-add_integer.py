#!/usr/bin/python3
"""a function to add two numbers"""


def add_integer(a, b=98):
    """a function that adds 2 integers

    ``a`` is the first value
    ``b`` is the second value
    returns a + b
    """
    if a is None or isinstance(a, (int, float)) is not True:
        raise TypeError("a must be an integer")
    elif b is None or isinstance(b, (int, float)) is not True:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
