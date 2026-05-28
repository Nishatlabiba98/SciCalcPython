import unittest
import math
from calculator import Calculator

class TestCoreFeatures (unittest.TestCase) :
    def setUp(self):
        self.calc = Calculator()

    def test_initial_state(self):
        self.assertEqual(self.calc.state, 0)
    def test_add_twonumbers(self):
        self.assertEqual(self.calc.add(3, 3), 6)
    def test_subtract_twonumbers(self):
        self.assertEqual(self.calc.subtract(10, 4), 6)
    def test_multiply_twonumbers(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)
    def test_divide_twonumbers(self):
        self.assertEqual(self.calc.divide(40, 5), 8)
    def test_sine(self):
        self.calc.state = 90
        self.assertAlmostEqual(self.calc.sine(), 1.0, places =5)
    def test_cosine(self):
        self.calc.state = 0
        self.assertAlmostEqual(self.calc.cosine(), 1.0, places =5)
    def test_tangent(self):
        self.calc.state = 45
        self.assertAlmostEqual(self.calc.tangent(), 1.0, places = 5)

if __name__ == '__main__':
    unittest.main()
