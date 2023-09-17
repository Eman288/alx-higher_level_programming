#!/usr/bin/python3
"""the module for the base class"""


class Base:
    """the base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """a function to set the id"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
