#!/usr/bin/python3
"""a function to add two numbers"""


def add_integer(a, b=98):
    """a function that adds 2 integers

    ``a`` is the first value
    ``b`` is the second value
    returns a + b
    """
    if a is None:
        raise TypeError("a must be an integer")
    elif b is None:
        raise TypeError("b must be an integer")
    try:
        a = a + 0
    except (TypeError, ValueError):
        raise TypeError("a must be an integer")
    try:
        b = b + 0
    except (TypeError, ValueError):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
