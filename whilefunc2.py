# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 08:58:12 2023

@author: Usman Ahmad
"""

values =[]
def main():
 options()   
 usr =0
 while usr !=6:
     usr = int(input("Enter a number:"))
     if usr ==1:
         add()
         options()
     elif usr ==2:
         search()
         options()
     elif usr ==3:
         rem()
         options()
     elif usr ==4:
         max1()
         options()
     elif usr ==5:
         min1()
         options()
     else:
         break

def add():

 print("Enter  a number: (Q for exit):")
 x = input("")
 while x.upper() !="Q":
    values.append(int(x))
    x = input("")
    if x.upper()=="Q":
        print(values)
        print(sum(values))
        break
    
    
def search():
   x  = int(input("Search for a number:"))    
   if x in values:
       print("Results found:",x , " in position:", values.index(x))
   else:
       print("Results not found!")
     
def rem():
 print("Remove an element:")
 y = int(input("Enter a number:"))   
 values.remove(y)
 print(values)        
 
def max1():
     print("max value in the list:",max(values))
def min1():
     print("min value in the list:",min(values))       
       
       
    
def options():
 print("1--->Add numbers")
 print("2--->Search numbers")
 print("3--->Remove an element")
 print("4 --->Find the maximum value")
 print("5 --->Find the minimum value")
 print("6--->Exit")
main()