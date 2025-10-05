import unittest
from simple_calculator import SimpleCalculator

class TestClass(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(2,3),5)
        self.assertEqual(self.calc.add(1,0),1)
        self.assertEqual(self.calc.add(-1,1),0)
        self.assertEqual(self.calc.add(0,0),0)
        self.assertEqual(self.calc.add(-10,-5),-15)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(2,3),-1)
        self.assertEqual(self.calc.subtract(1,0),1)
        self.assertEqual(self.calc.subtract(-1,1),-2)
        self.assertEqual(self.calc.subtract(0,0),0)
        self.assertEqual(self.calc.subtract(-10,-5),-5)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(2,3),6)
        self.assertEqual(self.calc.multiply(1,0),0)
        self.assertEqual(self.calc.multiply(-1,1),-1)
        self.assertEqual(self.calc.multiply(0,0),0)
        self.assertEqual(self.calc.multiply(-10,-5),50)

    def test_division(self):
        self.assertEqual(self.calc.divide(9,3),3)
        self.assertEqual(self.calc.divide(1,0),None)
        self.assertEqual(self.calc.divide(-1,1),-1)
        self.assertEqual(self.calc.divide(0,0),None)
        self.assertEqual(self.calc.divide(-10,-5),2)

if __name__ == "__main__":
    unittest.main()