#!/usr/bin/python3
"""a module of a class inherits from list"""


class MyList(list):
    """ a class that inherits from list"""

    def __init__(self):
        super().__init__()

    def print_sorted(self):
        return (sorted(self))
