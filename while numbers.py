# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 09:24:12 2023

@author: Usman Ahmad
"""
num = int(input('input a  number (0 for exit):'))
sum =0

n=0
while num !=0:
 if num > 0:
         sum = sum + num 
         n=n+1
         avg = sum/n
         m1 = max(num, num)
         num = int(input('input a  number (0 for exit):'))
         print('average:',avg)
         print('max:',m1)
         
 else:
    print('Test')