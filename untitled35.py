# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 12:26:53 2023

@author: Usman Ahmad
"""

num = int(input('Enter a number:'))
sum=0
n=0

while num !=0:
 if num >0:
     sum = sum+num
     n = n+1
     avg = sum/n
     num = int(input('Enter a number:'))
print(sum) 
print(avg)    
        