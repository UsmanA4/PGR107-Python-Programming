# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 13:14:39 2023

@author: Usman Ahmad
"""
pass1=987654321
password=0
account =10000
name1 ='Usman'
name = ''
while password !=pass1 and name !=name1 :
 name =input('What is your name:')   
 password = int(input('What is your password?'))
 print('Invalid name or password please try again')
 
 if password == pass1:
     y=input("Hi There! , do you want to  take out money?")
     if y =='yes':
         s = int(input('Enter a number to take out money:'))
         left = account - s 
         print("You have:", left , 'in your account after takeout')
         
     else:
      print("OK Bye!") 
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      