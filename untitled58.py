# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 09:49:03 2023

@author: Usman Ahmad
"""


print("Chinese zodiac asign")
year = int(input("Enter a year:"))

if year ==2000:
    animal = "Dragon"
elif year ==2001:
 animal = "Snake"    
 
elif year ==2002:
     animal = "Horse"
     
elif year ==2003:
 animal = "Sheep"    
elif year ==2004:
  animal = "Monkey"    
elif year ==2005:
 animal = "Rooster"       
elif year ==2006:
 animal = "Dog"      
elif year ==2007:
 animal = "Pig"     
elif year ==2008:
  animal = "Rat"     
elif year ==2009:
    animal ="Ox"
elif year ==2010:
 animal = "Tiger"     
elif year == 2011:
    animal ="Hare"
else: 
    year =0
    print("Invalid input!!")
if year !=0:
  print(year, "|", animal)    
    