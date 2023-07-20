# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 16:23:44 2023

@author: Usman Ahmad
"""
num =0
sum=0
fn = input('Input firstname:')
ln= input('Input lastname:')

while num !=-1:
  num+=int(input('Enter positive numbers:'))
  sum += num
  avg = sum/num
  
  
  if num ==-1:
      break 
  print(avg)

       
     