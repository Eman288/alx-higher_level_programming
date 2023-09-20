#!/usr/bin/python3
"""Rectangle module"""


from models.base import Base
"""the base module"""


class Rectangle(Base):
    """the Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initiate the values"""
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.width = width
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.height = height
        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.x = x
        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.y = y
        Base.__init__(self, id)

    @property
    def width(self):
        """get the width"""
        return self.__width

    @width.setter
    def width(self, width):
        """set the width"""
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """get the height"""
        return self.__height

    @height.setter
    def height(self, height):
        """set the height"""
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """get the x"""
        return self.__x

    @x.setter
    def x(self, x):
        """set the x"""
        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """get the y"""
        return self.__y

    @y.setter
    def y(self, y):
        """set the y"""
        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("x must be >= 0")
        self.__y = y

    def area(self):
        """return the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """display the rectangle in a # form"""
        for virtical in range(self.__y):
            print('')
        for i in range(self.__height):
            for hori in range(self.__x):
                print(' ', end="")
            for j in range(self.__width):
                print("#", end="")
            print('')

    def __str__(self):
        """dispaly the Rectangle"""
        s = "[Rectangle] ({}) {}/{} - {}/{}"
        m = s.format(self.id, self.__x, self.__y, self.__width, self.__height)
        return m

    def update(self, *args, **kwargs):
        """a function to update the values"""
        if args is not None and len(args) != 0:
            j = 0
            for i in args:
                if j == 0:
                    self.id = i
                    j += 1
                elif j == 1:
                    self.__width = i
                    j += 1
                elif j == 2:
                    self.__height = i
                    j += 1
                elif j == 3:
                    self.__x = i
                    j += 1
                elif j == 4:
                    self.__y = i
                    j += 1
        for i in kwargs:
            if i == "id":
                self.id = kwargs.get(i)
            elif i == "width":
                self.__width = kwargs.get(i)
            elif i == "height":
                self.__height = kwargs.get(i)
            elif i == "x":
                self.__x = kwargs.get(i)
            elif i == "y":
                self.__y = kwargs.get(i)
    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        return {'id': self.id, 'width': self.width, 'height': self.height,
            'x': self.x, 'y': self.y}
