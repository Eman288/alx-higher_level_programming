#!/usr/bin/python3
""" a module that has the is_same_class function"""


def is_same_class(obj, a_class):
    """afunction
    that check if an obj is of type of the class
    """
    if type(obj) == a_class:
        return True
    return False
