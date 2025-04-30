##
# @file stddev.py
# @author xmacekd00
# @brief: Stddev.py calculates sample standart deviation.
#              Program reads data from file given to stdin.
# @date 16.04.2025
#@details Program reads data from stdin 

import math_lib
import sys
import os

def get_resource_path(relative_path):
    """
    @brief Get absolute path to resource, works for dev and for PyInstaller
    """
    if getattr(sys, 'frozen', False):  # Running as compiled exe
        base_path = sys._MEIPASS  # PyInstaller temp folder
    else:  # Running as normal Python script
        base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, relative_path)

def load_input_data():
    """
    @brief Load data either from stdin or bundled file
    """
    try:
        if not sys.stdin.isatty():  # Check if input is being piped
            return sys.stdin.read()
        else:  # Fall back to bundled file
            input_path = get_resource_path('input.txt')
            with open(input_path, 'r') as f:
                return f.read()
    except FileNotFoundError:
        print("Error: Could not find input.txt", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error reading input: {str(e)}", file=sys.stderr)
        sys.exit(1)

file_data= load_input_data()

numbers=[]
for number in file_data.split(): #split the whole file by most common white space
    numbers.append(float(number))

sum_of_squared_numbers = 0
sum=0
for number in numbers:  #calculate sum of numbers and sum of squared numbers
    number_squared=math_lib.power(number,2)
    sum_of_squared_numbers= math_lib.add(sum_of_squared_numbers,number_squared)
    sum=math_lib.add(sum,number)
average=math_lib.divide(sum,len(numbers))
#ted to v zavorce
in_brackets=math_lib.subtract(sum_of_squared_numbers,math_lib.multiply(len(numbers),math_lib.power(average,2))) #result of the expression in brackets 
under_squareroot=math_lib.divide(in_brackets,len(numbers)-1)  # result of expression under squareroot
stddev=math_lib.nth_root(under_squareroot,2) # result 

print(stddev)

