# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 11:56:57 2023

@author: Usman Ahmad
"""

num = int(input('Enter a number(0 for exit):'))
sum =0
n=0
min =num
max = num
while num !=0:
    if num >max:
        max=num
    elif num <min:
         min =num
    n=n+1
    sum = sum+num
    num = int(input('Enter a number(0 for exit):'))
avg = sum/n
rng = max-min

print('Average:',avg)
print("Largest:", max)
print("Smallest:", min)     
    