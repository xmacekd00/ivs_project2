## ================================================
# File: stddev.py
# Authors: xmacekd00
# Description: Stddev.py calculates sample standart deviation.
#              Program reads data from file given to stdin.
# Creation date: 2025-04-16
# Version: 1
# ================================================
import calc
import sys

file_data= sys.stdin.read() #load whole file

numbers=[]
for number in file_data.split(" "): #split the whole file by character " " and load array of numbers
    numbers.append(float(number))

sum_of_squared_numbers = 0
sum=0
for number in numbers:  #calculate sum of numbers and sum of squared numbers
    number_squared=calc.power(number,2)
    sum_of_squared_numbers= calc.add(sum_of_squared_numbers,number_squared)
    sum=calc.add(sum,number)
average=calc.divide(sum,len(numbers))
#ted to v zavorce
in_brackets=calc.subtract(sum_of_squared_numbers,calc.multiply(len(numbers),calc.power(average,2))) #result of the expression in brackets 
under_squareroot=calc.divide(in_brackets,len(numbers)-1)  # result of expression under squareroot
stddev=calc.nth_root(under_squareroot,2) # result 

print(stddev)

