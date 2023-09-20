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

    def update(self, *args, **kwargs):
        """a function to update the values"""
        if args is not None and len(args) != 0:
            j = 0
            for i in args:
                if j == 0:
                    self.id = i
                    j += 1
                elif j == 1:
                    self.width = i
                    self.height = i
                    j += 1
                elif j == 2:
                    self.x = i
                    j += 1
                elif j == 3:
                    self.y = i
                    j += 1
        for i in kwargs:
            if i == "id":
                self.id = kwargs.get(i)
            elif i == "size":
                self.width = kwargs.get(i)
                self.height = kwargs.get(i)
            elif i == "x":
                self.x = kwargs.get(i)
            elif i == "y":
                self.y = kwargs.get(i)

    def to_dictionary(self):
        """returns the dictionary representation of a square"""
        return {'id': self.id, 'size': self.width, 'x': self.x, 'y': self.y}
