# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 10:13:33 2023

@author: Usman Ahmad
"""


import math
def fact(num):
    n =1
    x=num
    for i in range(1, n+1):
     print("The factorial is:", end=(" "))
    print(math.factorial(x)) 
fact(5)    