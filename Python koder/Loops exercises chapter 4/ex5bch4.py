# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 10:58:02 2023

@author: Usman Ahmad
"""

s = input('Type in a string:')
i=0
result=""
for char in s:
    if i %2==0:  
        result = result+ str(char)
    i=i+1
    print(result)