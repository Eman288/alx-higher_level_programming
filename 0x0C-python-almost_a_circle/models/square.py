#!/usr/bin/python3
"""Rectangle module"""


from models.rectangle import Rectangle
"""the rectangle module"""


class Square(Rectangle):
    """the square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """the initiation function"""
        Rectangle.__init__(self, size, size, x, y)
    
    def __str__(self):
        """display ther square"""
        s = "[Square] ({}) {}/{} - {}"
        m = s.format(self.id, self.x, self.y, self.width)
        return m