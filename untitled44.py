# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 09:05:47 2023

@author: Usman Ahmad
"""

def main():
 x=0
 while x !=3:
  x = int(input("Enter a number (3 for exit):"))
  if x == 1:
      bank()
  else:
      break


def bank():
   password =123456
   account =45000
   x=0
   while x!=password:
    x = int(input('Enter your password:'))
    if  x==password :
     y = int(input('how much do you want to take out?'))      
     take = print("You have now :",account-y , " in your bank account")
     return take

    else:
        print('Invalid input!!!')

    
   
main()   