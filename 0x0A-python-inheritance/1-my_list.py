#!/usr/bin/python3
"""a module of a class inherits from list"""


class MyList(list):
    """ a class that inherits from list"""

    def print_sorted(self):
        print(sorted(self))
