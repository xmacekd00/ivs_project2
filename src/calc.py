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
	result = 1
	for i in range(1, n + 1):
		result *= i
	return result

def power(a, b):
	return a**b

def nth_root(a, n):
	if( a < 0 and n%2==0):
		raise ValueError("Negative input not allowed for root function!")
	if a < 0:
		return -((-a) ** (1 / n)) # odd root of negative number
	return a ** (1 / n)

def modulo(a, b):
	if b == 0:
		raise ZeroDivisionError("Modulo by zero is undefined!")
	return a % b
def truncate(a, b):
	number=str(a)
	rounded_number=""
	decimal_place=False
	decimal_place_counter=0

	for i in range(0,len(number)):
		rounded_number = rounded_number + number[i]
		if decimal_place==True: decimal_place_counter+=1	#increase decimale_palce_counter with every digit in decimal place
		if decimal_place_counter== b: break
		if number[i] == ".": decimal_place= True

	return float(rounded_number)
