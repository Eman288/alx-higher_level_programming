#!/usr/bin/python3
"""Rectangle module"""


from models.rectangle import Rectangle
"""the rectangle module"""


class Square(Rectangle):
    """the square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """the initiation function"""
        Rectangle.__init__(self, size, size, x, y, id)

    def __str__(self):
        """display ther square"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

    @property
    def size(self):
        """a function to return the size"""
        return self.width

    @size.setter
    def size(self, val):
        """a function to set the width and the height with size"""
        self.width = val
        self.height = val
