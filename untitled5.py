# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 11:00:09 2023

@author: Usman Ahmad
"""


s =input('Enter a string:')
# if the string contains only letters

if s.isalpha():
  print("This string contains letters only ")

if s.isdigit():
    print("The string contains digits only")
    #If the string contains letters and numbers
if s.isalnum():
   print("The string contains both letters and digits")  
   #If the string is uppercase only 
if  s.isupper():
    print("The string is uppercase only")
    #If the string is lowercase only 
if s.islower():
 print('The string is only in lowercase')
if s[0].isupper():
 print("The string starts with an uppercase letter")  
if s.endswith('.'):
    print("The string ends with a period")
    
    #End of code----