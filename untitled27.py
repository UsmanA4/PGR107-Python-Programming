# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 17:28:53 2023

@author: Usman Ahmad
"""

count = 0
sum = 0.0
number = 1
	
while number != -1:
	    number = int(input(""))
	    sum = sum + number
	    count += 1
	
if count == 0:
	    print("Input some numbers")
else:
	    print("Average and Sum of the above numbers are: ", sum / (count-1), sum)
