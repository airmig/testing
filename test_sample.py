"""
unit tests for sample.py
python -m unittest test_sample.py
"""
import unittest

from sample import doubler, square

class TestSample(unittest.TestCase):
    """
    Unit test class for sample module
    """
    def test_square(self):
        """
        tests for square function
        """
        self.assertEqual(square(5), 25)
    
    def test_doubler(self):
        """
        test for doubler function
        """
        self.assertEqual(doubler(10), 20)