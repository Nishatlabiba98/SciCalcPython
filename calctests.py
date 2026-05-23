import unittest
import math
from calculator import Calculator

class TestCoreFeatures (unittest.TestCase) :
    def setUp(self):
        self.calc = Calculator()

    def test_add2(self):
        self.assertEqual(self.calc.add(12, -10), 2)

    def test_add3(self):
        self.assertEqual(self.calc.add(5, 8), 13)

    def test_sub(self):
        self.assertEqual(self.calc.sub(9, 3), 6)


if __name__ == '__main__':
    unittest.main()
