# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 11:20:25 2023

@author: Usman Ahmad
"""

#ex5ech4
pos =0
result=""
s = input('Input string:')
for i in s:
     
 if i in  {'a', 'e' , 'i', 'o', 'u' , 'U', 'O' , 'A', 'E', 'I'}:
     
    result = result + str(pos)
    print("output:",result)
    pos=pos +1
         