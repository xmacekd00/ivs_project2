##
# @file calc.py
# @author xperuta00, xmacekd00
# @brief Unit tests for math lib calc.py
# @date 1.04.2025
import unittest
from math_lib import add, subtract, multiply, divide, factorial, power, nth_root, modulo, truncate, evaluate

##
#@brief Class contains unittests for math lib
class TestCalc(unittest.TestCase):
    ##
    #@brief Adition test
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(-1, -1), -2)

    ##
    #@brief Subtraction test
    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(3, 5), -2)
        self.assertEqual(subtract(0, 5), -5)
        self.assertEqual(subtract(-1, -1), 0)
    ##
    #@brief Multiplication test
    def test_multiply(self):
        self.assertEqual(multiply(4, 3), 12)
        self.assertEqual(multiply(0, 100), 0)
        self.assertEqual(multiply(-2, 3), -6)

    ##
    #@brief Division test
    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertAlmostEqual(divide(7, 2), 3.5)
        with self.assertRaises(ZeroDivisionError): 
            divide(5, 0)

    ##
    #@brief Factorial test
    def test_factorial(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(3), 6)
        self.assertEqual(factorial(5), 120)
        with self.assertRaises(ValueError):
            factorial(-1)

    ##
    #@brief Exponentiation by natural exponent
    def test_power(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 0), 1)
        self.assertEqual(power(7, 2), 49)
        self.assertEqual(power(3, 1), 3)

    ##
    #@brief Find nth root
    def test_nth_root(self):
        self.assertEqual(nth_root(27, 3), 3)
        self.assertEqual(nth_root(16, 4), 2)
        # aproximacia 2ky
        self.assertAlmostEqual(nth_root(2, 2), 1.41421356, places=5)
        with self.assertRaises(ValueError):
            # zaporna odmocnina
            nth_root(-8, 2)

    ##
    #@brief Modulo test
    def test_modulo(self):
        self.assertEqual(modulo(10, 3), 1)
        self.assertEqual(modulo(10, 5), 0)
        self.assertEqual(modulo(10, 7), 3)
        with self.assertRaises(ZeroDivisionError):
            modulo(10, 0)
    ##
    #@biref Test of truncate
    def test_truncate(self):
        self.assertEqual(truncate(0.555555,5),0.55555)
        self.assertEqual(truncate(1,5),1)
        self.assertEqual(truncate(1.11,0),1)
        with self.assertRaises(ValueError):
            truncate(1,-2)

    ##
    #@brief Evaluation test
    def test_evaluate(self):
        #random test values
        self.assertEqual(evaluate("5!"), 120)
        self.assertEqual(evaluate("-3*-2"), 6)
        self.assertEqual(evaluate("3*3n-8"), -6)
        self.assertEqual(evaluate("2S"), 4)
        self.assertEqual(evaluate("s4"), 2)
        self.assertEqual(evaluate("3N-3"), 1/27)
        #basic test for all functions
        self.assertEqual(evaluate("2N3"), 8)
        self.assertEqual(evaluate("3n8"), 2)
        self.assertEqual(evaluate("5S"), 25)
        self.assertEqual(evaluate("s4"), 2)
        self.assertEqual(evaluate("5!"), 120)
        self.assertEqual(evaluate("5*2"), 10)
        self.assertEqual(evaluate("10/2"), 5)
        self.assertEqual(evaluate("10M3"), 1)
        self.assertEqual(evaluate("5+2"), 7)
        self.assertEqual(evaluate("5-2"), 3)
        #more complex inputs
        self.assertEqual(evaluate("2N3+5*2"), 18)
        self.assertEqual(evaluate("5!/10"), 12)
        self.assertEqual(evaluate("s9+1"), 4)
        self.assertEqual(evaluate("10M3-1"), 0)
        #decimal numbers
        self.assertEqual(evaluate("2.5*4"), 10)
        #operations with negative numbers
        self.assertEqual(evaluate("-5+2"), -3)
        self.assertEqual(evaluate("5*-2"), -10)
        #fact edge case
        self.assertEqual(evaluate("0!"), 1)
        #Exceptions and errors
        with self.assertRaises(ZeroDivisionError):
            evaluate("5/0")

        with self.assertRaises(ZeroDivisionError):
            evaluate("5M0")

        with self.assertRaises(ValueError):
            evaluate("-5!")

        with self.assertRaises(ValueError):
            evaluate("2n-8")

        
if __name__ == '__main__':
    unittest.main()
## end of tdd.py