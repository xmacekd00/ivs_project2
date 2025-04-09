import math

def add(a, b):
    return a + b

# the following functions have not been implemented 
def subtract(a, b):
	return a - b

def multiply(a, b):
	return a * b

def divide(a, b):
	if b == 0:
		raise ZeroDivisionError("Division by zero is undefined!")
	return a / b

def factorial(n):
	if n < 0:
		raise ValueError("Factorial is not defined for negative numbers!")
	return math.factorial(n)

def power(a, b):
	return a**b

def nth_root(a, n):
	if a < 0:
		raise ValueError("Negative input not allowed for root function!")
	return a ** (1 / n)

def modulo(a, b):
	if b == 0:
		raise ZeroDivisionError("Modulo by zero is undefined!")
	return a % b
