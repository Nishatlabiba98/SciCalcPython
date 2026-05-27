import unittest
import math
from calculator import Calculator

class TestCoreFeatures (unittest.TestCase) :
    def setUp(self):
        self.calc = Calculator()

    def test_initial_state(self):
        self.assertEqual(self.calc.state, 0)
    


