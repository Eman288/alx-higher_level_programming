#!/usr/bin/python3
"""defintion of a class"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """a class of square"""
    def __init__(self, size):
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size * self.__size
