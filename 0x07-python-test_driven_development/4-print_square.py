#!/usr/bin/python3
"""a function to print a square"""


def print_square(size):
    """a function to print a square of #

    size => the size of the square
    """
    if isinstance(size, int) is not True:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(0, size):
        for j in range(0, size):
            print("#", end="")
        print('')
