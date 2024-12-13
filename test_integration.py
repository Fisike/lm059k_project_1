# test_integration.py

import unittest
from program import Calculator

class TestCalculatorIntegration(unittest.TestCase):
    def test_combined_operations(self):
        calc = Calculator()
        result = calc.add(calc.multiply(2, 3), 4)  # (2*3) + 4
        self.assertEqual(result, 10)

if __name__ == '__main__':
    unittest.main()
