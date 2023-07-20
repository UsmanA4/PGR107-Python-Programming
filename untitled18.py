# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 19:53:21 2023

@author: Usman Ahmad
"""
print("Calculate the area and the perimeter of a rectangle below")
a= float(input("Skriv et tall for bredden:"))
b = float(input("Skeiv et tall for høyden:"))

if a>b:
 area = (a*b)
 per= 2*(a+b)
 print("The area of the rectangle is:", area)
 print("The perimeter of the rectangle is:", per)
 
else:
    print("Invalid numbers")

