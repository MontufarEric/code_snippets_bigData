import unittest
from Calculator import Calculator as calc


class TestCalc(unittest.TestCase):


    def test_add(self):
        self.assertEqual(calc.add(1, 5), 6)
        self.assertEqual(calc.add(-1, 2), 1)
        self.assertEqual(calc.add(-1, -3), -4)

    def test_subtract(self):
        self.assertEqual(calc.subtract(10, 2), 8)
        self.assertEqual(calc.subtract(-1, 3), -4)
        self.assertEqual(calc.subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(calc.multiply(10, 3), 30)
        self.assertEqual(calc.multiply(-1, 2), -2)
        self.assertEqual(calc.multiply(-1, -2), 2)

    def test_divide(self):
        self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.divide(-1, 1), -1)
        self.assertEqual(calc.divide(-1, -1), 1)
        self.assertEqual(calc.divide(5, 2), 2.5)

            
if __name__ == '__main__':
    unittest.main()
