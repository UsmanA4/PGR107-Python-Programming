# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 11:47:48 2023

@author: Usman Ahmad
"""

num = int(input('Enter a number:'))
sum =0
n =0
while num !=0:
    if num >0:
     sum = sum+num
     max=num
     min =num
     n=n+1
     avg = sum/n
     num = int(input('Enter a number:'))
     rng = max-min
print("Average:", avg)     
print("Sum:",sum)
print("Max:",max )
print("Min:",min)      
print('Range:',rng)  