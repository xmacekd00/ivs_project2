import unittest
from calc import add, subtract, multiply, divide, factorial, power, nth_root, modulo

class TestCalc(unittest.TestCase):
    # tests for basic functions
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(3, 5), -2)
        self.assertEqual(subtract(0, 5), -5)
        self.assertEqual(subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(multiply(4, 3), 12)
        self.assertEqual(multiply(0, 100), 0)
        self.assertEqual(multiply(-2, 3), -6)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertAlmostEqual(divide(7, 2), 3.5)
        with self.assertRaises(ZeroDivisionError): 
            divide(5, 0)

    # faktorial
    def test_factorial(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(3), 6)
        self.assertEqual(factorial(5), 120)
        with self.assertRaises(ValueError):
            factorial(-1)

    # umocnovanie s prirodzenymi exponentmi
    def test_power(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 0), 1)
        self.assertEqual(power(7, 2), 49)
        self.assertEqual(power(3, 1), 3)

    # n-ta odmocnina
    def test_nth_root(self):
        self.assertEqual(nth_root(27, 3), 3)
        self.assertEqual(nth_root(16, 4), 2)
        # aproximacia 2ky
        self.assertAlmostEqual(nth_root(2, 2), 1.41421356, places=5)
        with self.assertRaises(ValueError):
            # zaporna odmocnina
            nth_root(-8, 3)

    # modulo - volitelna funkcia
    def test_modulo(self):
        self.assertEqual(modulo(10, 3), 1)
        self.assertEqual(modulo(10, 5), 0)
        self.assertEqual(modulo(10, 7), 3)
        with self.assertRaises(ZeroDivisionError):
            modulo(10, 0)

if __name__ == '__main__':
    unittest.main()
