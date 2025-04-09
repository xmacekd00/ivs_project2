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
		raise ZeroDivisionError("Division by zero is undefined.")
	return a / b

def factorial(n):
	if n < 0:
		raise ValueError("Factorial is not defined for negative numbers!")
	return math.factorial(n)

def power(a, b):
    raise NotImplementedError("power is not implemented yet.")

def nth_root(a, n):
    raise NotImplementedError("nth_root is not implemented yet.")

def modulo(a, b):
    raise NotImplementedError("modulo is not implemented yet.")
