# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 10:08:00 2023

@author: Usman Ahmad
"""


#Functions
def numbers():
    num1=int(input('Enter a number:'))
    num2= int(input('Enter a second number:'))
    n=1
    sum=0
    n=n+1
    sum = num1 + num2
    avg = sum/n
    m1 = max(num1,num2)
    m2 = min(num1,num2)
    print('Sum:',sum)
    print('Max:', m1)
    print('Min:',m2)
    print('Average:', avg)
      
   
numbers()    
   