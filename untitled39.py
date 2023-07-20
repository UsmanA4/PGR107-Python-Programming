# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 11:48:41 2023

@author: Usman Ahmad
"""

num = float(input("Enter a number (0 for exit): "))
# sum of all numbers 
sum = 0 
# number of entered numbers 
n = 0
# initialize min and max with first input
min = num
max = num

# 0 is sentinel value 
while num != 0:
    # update min and max 
    if num > max:
        max = num
    elif num < min:
        min = num
    # increment number of inputs
    n = n + 1 
    # add current number to sum 
    sum = sum + num
    # new user input
    num = float(input("Enter a number (0 for exit): "))
    
# calculate average value 
average = sum / n
# calculate range 
rng = max - min

# print results
print("Average of the values: " + str(average))
print("The smallest value is: " + str(min))
print("The largest value if: " + str(max))
print("The range is: " + str(rng))