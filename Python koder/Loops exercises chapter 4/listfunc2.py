# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 09:45:35 2023

@author: Usman Ahmad
"""

list1 = [1,2,3,4,5,6,7,980,1096]

def main():
  print(list1)
  options()
  x = 0
  while x !=6:
      x = int(input("Enter a number:"))
      if x ==1:
          search()
          options()
      elif x==2:
          app()
          options()
      elif x==3 :
          rem()
          options()
      elif x==4:
          max1()
          options()
      elif x==5:
          min1()
          options()
      else:
          print("Stop!")
          break
    

def search():
  
  x = int(input("Search for a value:"))
  if x in list1:
      print("Results found:",x, " in position:", list1.index(x))
  else:
      print("Results not found!!")
  

def app():
 y = int(input("Enter a number to append:"))
 list1.append(y)    
 print(list1)

def rem():
 r = int(input("Remove an element:"))
 print("Removed from index:",list1.index(r))
 list1.remove(r)
 print(list1)
 
def max1():
    print("The maximum value in the list is:")  
    print(max(list1))
def min1():
  print("The minimum value in the list is:")  
  print(min(list1))    
def options():
    print("1---> Search for an element")
    print("2---> Append an element")
    print("3---> Remove an element ")
    print("4---> Find max value")
    print("5---> Find min value ")
    print("6---> Exit")

main() 