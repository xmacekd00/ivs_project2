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

def evaluate(equation):
        """Evaluates the equation in string"""
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

