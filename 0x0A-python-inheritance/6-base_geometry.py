#!/usr/bin/python3
"""defintion of the class"""


class BaseGeometry:
    """a class with a method that raise an exception"""
    def area(self):
        raise Exception("area() is not implemented")

