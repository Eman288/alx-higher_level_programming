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

    if __name__ == "__main__":
        unittest.main()
