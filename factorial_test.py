# Run with 'python factorial_test.py' or 'python -m unittest discover -p '*_test.py'

import unittest
from factorial import fact, div

class TestFactorial(unittest.TestCase):
    """Any method which starts with `test_` will be considered as a test case."""

    def test_fact(self):
        """It correctly returns the resulf of 5 factorial."""

        res = fact(5)
        self.assertEqual(res, 120)

    def test_div(self):
        """It raises a ZeroDivisionError when trying to divide by zero."""

        self.assertRaises(ZeroDivisionError, div, 0)

if __name__ == '__main__':
    unittest.main()

