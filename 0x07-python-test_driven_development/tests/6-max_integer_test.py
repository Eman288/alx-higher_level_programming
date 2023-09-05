#!/usr/bin/python3
"""Unittest for max_integer([..])"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """a class to test with unittest"""

    def test_normal(self):
        """a function to test the function on normal list"""
        mat = [1, 3, 44, 6]
        self.assertAlmostEqual(max_integer(mat), 44)

    def test_normal2(self):
        """a function to test the function on normal list2"""
        mat = [2, 5, 6, 8]
        self.assertAlmostEqual(max_integer(mat), 8)

    def test_empty(self):
        """a function to test the function on empty list"""
        mat = []
        self.assertAlmostEqual(max_integer(mat), None)

    def test_floats(self):
        """a function to test the function on float list"""
        mat = [2.4, 77.6, 32.2, 0.993]
        self.assertAlmostEqual(max_integer(mat), 77.6)

    def test_float_int(self):
        """a function to test the function on float and int list"""
        mat = [5.88, 0, 2.763, 3]
        self.assertAlmostEqual(max_integer(mat), 5.88)

    def test_str(self):
        """a function to test the function on string list"""
        mat = "hello world"
        self.assertAlmostEqual(max_integer(mat), 'w')

    def test_strings(self):
        """a function to test the function on strings list"""
        mat = ["hello", "welcome", "name", "is", "someone"]
        self.assertAlmostEqual(max_integer(mat), 'welcome')

    if __name__ == '__main__':
        unittest.main()
