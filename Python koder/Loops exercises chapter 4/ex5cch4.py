# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 11:08:48 2023

@author: Usman Ahmad
"""

s = input('String:')
result =""
for i in s:
    
    if i in {'a', 'e' , 'i', 'o', 'u' , 'U', 'O' , 'A', 'E', 'I'}:
        i = i +"_"
        result = result+ str(i)
        print(result)
