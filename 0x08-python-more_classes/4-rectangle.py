#!/usr/bin/python3
"""a module to create a rectangle and be able to get info"""


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

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if isinstance(value, int) is not True:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if isinstance(value, int) is not True:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height + self.__width) * 2

    def __str__(self):
        mat = ""
        if self.__height == 0 or self.__width == 0:
            return mat
        for i in range(0, self.__height):
            for j in range(0,  self.__width):
                mat += '#'
            if (i != self.__height - 1):
                mat += '\n'
        return (mat)

    def __repr__(self):
        return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))
