#!/usr/bin/python3
"""test module for rectangle"""


import unittest
"""the module we will test with"""

from models.base import Base
"""the base class"""

from models.rectangle import Rectangle
"""the class we will test on"""


class TestRectangle_init(unittest.TestCase):
    """the main testing class"""

    def test_only_two(self):
        """a function to test two arguemnt condition"""
        a1 = Rectangle(10, 2)
        a2 = Rectangle(2, 10)
        self.assertEqual(a1.id, a2.id - 1)

    def test_only_three(self):
        """a function to test three arguemnt condition"""
        b = Rectangle(4, 5, 6)
        self.assertEqual(b.x, b.width + 2)

    def test_only_four(self):
        """a function to test four arguemnt condition"""
        c = Rectangle(8, 5, 1, 4)
        self.assertEqual(c.width, c.y + 4)
class TestRectangle_width(unittest.TestCase):
    """the class testing of width"""
    def test_str(self):
        """a function to test the str value"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
                Rectangle("fd", 2)
    
    def test_less_than_0(self):
        """a function to test if a number less than 0"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
                Rectangle(-3, 2)
                
    def test_equal_to_0(self):
        """a function to test if a number equal to 0"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
                Rectangle(0, 2)
                
class TestRectangle_height(unittest.TestCase):
    """the class testing of height"""
    def test_str(self):
        """a function to test the str value"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
                Rectangle(32, "dsa")
    
    def test_less_than_0(self):
        """a function to test if a number less than 0"""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
                Rectangle(3, -2)
                
    def test_equal_to_0(self):
        """a function to test if a number equal to 0"""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
                Rectangle(2, 0)
        
class TestRectangle_x(unittest.TestCase):
    """the class testing of x"""
    def test_str(self):
        """a function to test the str value"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
                Rectangle(4, 2, "fxd")
    
    def test_less_than_0(self):
        """a function to test if a number less than 0"""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
                Rectangle(3, 2, -3)
                
class TestRectangle_y(unittest.TestCase):
    """the class testing of y"""
    def test_str(self):
        """a function to test the str value"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
                Rectangle(4, 2, 3, "DSa")
    
    def test_less_than_0(self):
        """a function to test if a number less than 0"""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
                Rectangle(3, 2, 3, -3)

class TestRectangle_process(unittest.TestCase):
    """to test most of the process in the class"""
    def test_area(self):
        """a function to test area function in normal mode"""
        a = Rectangle(2, 3)
        self.assertEqual(a.area(), 6)

if __name__ == "__main__":
        unittest.main()
