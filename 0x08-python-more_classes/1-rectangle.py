#!/usr/bin/python3
"""a module to create a rectangle"""


class Rectangle:
    """
    a class to create a rectangle with width and hight
    """
    
    def __init__(self, width=0, height=0):
        """a function to initialize the variables
        width => the width
        height => the height
        """

        self.width = width
        self.height = height
    
    def width(self):
        """a function to get the width"""

        return __width
    
    def width(self, value):
        """a function to set the width with a vaalue"""

        if isinstance(value, int) is not True:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def height(self):
        """a function to get the height"""

        return __height

    def height(self, value):
        """a function to set the height with a vaalue"""
        
        if isinstance(value, int) is not True:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
