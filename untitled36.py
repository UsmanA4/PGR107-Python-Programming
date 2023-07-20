# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 07:32:17 2023

@author: Usman Ahmad
"""
score = int(input('Enter your score:'))
sum =0
n=0
while score !=-1:
    if score >-1:
     sum =sum+score 
     n = n+1
     avg = sum/n
     score = int(input('Enter your score:'))
print(avg)     
    
    
         