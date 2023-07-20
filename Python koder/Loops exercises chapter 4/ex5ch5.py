# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 08:10:40 2023

@author: Usman Ahmad
"""


def main():
    print('1 --> Convert celsius to fahrenheit')
    print('2 ---> Convert fahrenheit to celsius')
    print('3---> Exit')
    num =0
    while num !=3:
     num = int(input("Enter a number (3 for Exit):"))
     if num ==1:
      cf()
     elif num ==2:
      fc()
     else:
         print("STOP!")
         break
         
    

def cf(): #fahrenheit to celsius converter
    print('Fahrenheit to celcius converter')
    fahrenheit = float( input("Enter temperature in fahrenheit:"))
    celsius = (fahrenheit-32)/1.8
    print(fahrenheit," fahrenheit =",  celsius , " celsius")

    

def fc(): #celsius to fahrenheit converter
     print("Celsius to fahrenheit converter")
     celsius = float(input("Enter temperature in celsius:"))
     fahrenheit = (celsius*1.8)+32
     print(celsius," celsius =", fahrenheit , "  fahrenheit")
main()
         