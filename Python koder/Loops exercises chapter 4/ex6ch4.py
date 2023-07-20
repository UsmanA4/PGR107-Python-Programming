# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 11:47:48 2023

@author: Usman Ahmad
"""

num = float(input('Enter a number:'))
sum =0
n =0

max=num
min =num
while num !=0:
    if num >max:
        max=num
    elif num < min:
        min =num  
    n=n+1
    sum = sum+num
    num = float(input('Enter a number:'))
    
     
avg = sum/n  
rng = max-min  

  
print("Average:", avg)     
print("Sum:",sum)
print("Max:",max )
print("Min:",min)      
print('Range:',rng)  