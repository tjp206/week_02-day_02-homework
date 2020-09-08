import unittest
from src.calculator import add, subtract, divide, multiply

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(5, add(2, 3))
        # expected = 5       # this way also runs test
        # actual = add(2, 3)
        # self.assertEqual(expected, actual)
        
    def test_subtract(self):
        self.assertEqual(5, subtract(10, 5))

    def test_divide(self):
        self.assertEqual(2, divide(10, 5))

    def test_multiply(self):
        self.assertEqual(10, multiply(5, 2))