#!/usr/bin/python3
"""test file for the base class from the base module"""


import unittest
"""the unitest module to test"""

from models.base import Base
"""the class from the module we will test on"""

class TestBase_init(unittest.TestCase):
    """the main test class for the base class"""

    def test_no_argument(self):
        """a function to test for none arguments"""

        b1 = Base()
        b2 = Base()
        self.assertAlmostEqual(b1.id, b2.id - 1)
        self.assertAlmostEqual(b2.id, b1.id + 1)

    def test_there_is_argument(self):
        """a function to test for if we pass an argument"""

        b1 = Base(2)
        b2 = Base(3)
        self.assertAlmostEqual(b1.id, 2)
        self.assertAlmostEqual(b2.id, 3)

    def test_both_conditions(self):
        """a function to test both at the same time"""

        b1 = Base()
        b2 = Base(44)
        b3 = Base()
        self.assertAlmostEqual(b1.id, 1)
        self.assertAlmostEqual(b2.id, 44)
        self.assertAlmostEqual(b3.id, 2)

    if __name__ == "__main__":
        unittest.main()
