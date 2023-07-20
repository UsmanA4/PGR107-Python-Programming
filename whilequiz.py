# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 19:35:25 2023

@author: Usman Ahmad
"""

sum =0
print('Find the sum, the average, max and min--> 1')
print('\nMultiply numbers--> 2')
print('\nDevide numbers  -->3')

num = int(input('Enter a number (0 for exit):'))

while num !=0:
  if num ==1:
   from funnum import numbers
   numbers()
   num = int(input('Enter a number (0 for exit):'))

  elif num ==2:
       mu = int(input('Enter a number1:'))
       mu2 = int(input('Enter a second number2:'))
       
       p = mu*mu2
       print('mu*mu2=',p)
       num = int(input('Enter a number (0 for exit):')) 
  elif num ==3:
      n1 = int(input('Enter a number for the devision: '))
      n2 = int(input('Enter a second number:'))
      d = n1/n2
      print('n1/n2 =',d)
      num = int(input('Enter a number (0 for exit):'))
  else:
      print('This is a joke hahah, youve been scammed ')
      break



