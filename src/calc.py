##
# @file calc.py
# @author xperuta00, xmacekd00
# @brief Mathematical operations and equation solver
# @date 10.04.2025

def add(a, b):
	"""
	@brief Add two numbers
	@param a First number 
	@param b Second number
	@return Sum of a and b
	"""
	return a + b

# the following functions have not been implemented 
def subtract(a, b):
	"""
	@brief Subtrat two numbers
	@param a Minuend
	@param b Subtrahend
	@return Difference between a and b
	"""
	return a - b

def multiply(a, b):
	"""
	@brief Multiply two numbers
	@param a First factor
	@param b Second factor
	@return Product of a and b
	"""
	return a * b

def divide(a, b):
	"""
	@brief Divides two numbers
	@param a Dividend 
	@param b Divisor
	@return Quotient of a and b
	@throws ZeroDivisionError If b=0
	"""
	if b == 0:
		raise ZeroDivisionError("Division by zero is undefined!")
	return a / b

def factorial(n):
	"""
	@brief Calculates factorial of a number
	@param n  Positive integer
	@return Factorial of n
	@throws ValueError If n is negative
	"""
	if n < 0:
		raise ValueError("Factorial is not defined for negative numbers!")
	result = 1
	for i in range(1, n + 1):
		result *= i
	return result

def power(a, b):
	"""
	@brief Calculates nth power of a number
	@param a Base
	@param b Exponent
	@return a to the power of b
	"""
	return a**b

def nth_root(a, n):
	"""
	@brief Calculates the nth root of a number
	@param a Base, Positive number
	@param n Root number
	@return Nth root of a
	@throws ValueError If a is a negative number and n is even number 
	"""
	if( a < 0 and n%2==0):
		raise ValueError("Negative input not allowed for root function!")
	if a < 0:
		return -((-a) ** (1 / n)) # odd root of negative number
	return a ** (1 / n)

def modulo(a, b):
	"""
	@brief Calculates remainder of divion of two numbers
	@param a Dividend
	@param b Divisor
	@return Remainder of a and b
	@throws ZeroDivisionError If b=0
	"""
	if b == 0:
		raise ZeroDivisionError("Modulo by zero is undefined!")
	return a % b

def truncate(a, b):
	"""
	@brief Truncates number to specified decimal places
	@param a Number
	@param b NUmber of decimal places
	@return Number a with b decimal places or less
	"""
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

def evaluate(equation):
		"""
		@brief Evaluates an expression given in string format, operator N is Nth power (2N3=8)
																operator n is nth root (3n8=2)
																operator S is squared (5S=25)
																operator s is squareroot (s4=2)
		@param equation Expression to be calculated
		@return Value of the expression
		@throws ValueError For invalid input format
		@throws ZeroDivisionError For division by zero
		"""
		eq = equation
		eq=eq.replace(',','.')    #correct format of decimal point
	
		items = []  #array of numbers and operators
		i=0
		while i<len(eq):
			item=""  
			if eq[i].isdigit():    #item is a number
				while eq[i].isdigit() or eq[i] == ".":   #load all the digits 
					item+=eq[i] 
					i+=1
					if i>=len(eq): break   #end of equation check
				items.append(item)#add number to items
				
			else:   #item is an operator
				items.append(eq[i])
				i+=1

		i=0
		while i<len(items):
			if(items[i]=='-' and i==0):
				items[i]=str(multiply(float(items[i+1]),-1))
				del items[i+1]
			if(i+1<len(items) and items[i+1] == '-' ):
				if(items[i]=="S" or items[i]=="s" or items[i]=="N" or items[i]=="n" or items[i]=="M" or items[i]=="!" or items[i]=="+" or items[i]=="-"
				   or items[i]=="*" or items[i]=="/"):
					i+=1
					items[i]=str(multiply(float(items[i+1]),-1))
					del items[i+1]
			i+=1



		i=0
		#calculate special operations (fact, roots and powers)
		while i<len(items):
			match items[i]:
				case "n":
					tmp=nth_root(float(items[i+1]),float(items[i-1]))
					items[i]=str(tmp) # replace three arr items (operand (N), Nth root of x , operand(x)) with its result
					del items[i-1]
					del items[i]
					i-=2
				case "N": 
					tmp=power(float(items[i-1]),float(items[i+1]))
					items[i]=str(tmp) # replace three arr items (operand (N), Nth power of x , operand(x)) with its result
					del items[i-1]
					del items[i]
					i-=2
				case "S":
					tmp=power(float(items[i-1]),2)
					items[i]=str(tmp) # replace two arr items (x squared , operand(x)) with its result
					del items[i-1]
					i-=2
				case "s":
					tmp=nth_root(float(items[i+1],2))
					items[i]=str(tmp)
					del items[i-1]
					i-=2
				case "!":
					tmp=factorial(int(items[i-1]))
					items[i]=str(tmp) # replace two arr items (operand(x), !) with its result
					del items[i-1]
					i-=2
			i+=1
		i=0
		#calculate mult. division and modulo
		while i<len(items):
			match items[i]:
				case "*":
					tmp=multiply(float(items[i-1]),float(items[i+1]))
					items[i]=str(tmp) # replace three arr items (operand , *  , operand) with its result
					del items[i-1]
					del items[i]
					i-=2
				case "/":
					tmp=divide(float(items[i-1]),float(items[i+1]))
					items[i]=str(tmp) # replace three arr items (operand , / , operand) with its result
					del items[i-1]
					del items[i]
					i-=2
				case "M":
					tmp=modulo(float(items[i-1]),float(items[i+1]))
					items[i]=str(tmp) # replace three arr items (operand, %  , operand) with its result
					del items[i-1]
					del items[i]
					i-=2
			i+=1

		i=0
		#calculate add and sub
		while i<len(items):
			match items[i]:
				case "+":
					tmp=add(float(items[i-1]),float(items[i+1]))
					items[i]=str(tmp) # replace three arr items (operand, +  ,operand ) with its result
					del items[i-1]
					del items[i]
					i-=2
				case "-":
					tmp=subtract(float(items[i-1]),float(items[i+1]))
					items[i]=str(tmp) # replace three arr items (operand, - , operand) with its result
					del items[i-1]
					del items[i]
					i-=2
			i+=1
		return items[0]

## end of calc.py