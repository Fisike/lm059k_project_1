# test_unit.py

import unittest
from program import Calculator

class TestCalculatorUnit(unittest.TestCase):
    def test_add(self):
        calc = Calculator()
        self.assertEqual(calc.add(2, 3), 5)

    def test_multiply(self):
        calc = Calculator()
        self.assertEqual(calc.multiply(2, 3), 6)

if __name__ == '__main__':
    unittest.main()
