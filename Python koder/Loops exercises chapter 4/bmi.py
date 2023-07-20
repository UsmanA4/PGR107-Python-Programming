# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 09:41:02 2023

@author: Usman Ahmad
"""

def main():
  options()
  usr = 0
  while usr !=6:
   usr = int(input("Enter a number:"))
   if usr ==1:
        ticket()
        options()
   elif usr ==2:
        bmi()
        options()
   elif usr ==3:
       multi()
       options()
   elif usr ==4:
       factorial()
       options()
   elif usr ==5:
       exPower()
       options()
   else:     
        break

  

def ticket():
    bank=50000
    tvalue = 8700
    print("Your account balance:",bank)
    print("Price pr ticket:", tvalue)
    x = int(input("How many tickets do you want to order?"))
    take = bank -tvalue
    if x<=2 and x <take or x<=5:
        take1 =bank-(tvalue*x)
        print("Your order was successfully completed !")
        print("You have now:", take1, " in your account :)")
    else:
        print("Sorry not enough balance to order the tickets")

def bmi():
   x = int(input("Enter your weight:"))
   y = float(input("Enter your height:"))
   bmi = x/y**2
   print('Your BMI is:', bmi)
   if bmi <18.5:
       print("You are underweight")
   if bmi <18.5 or bmi < 25:
       print("You are normal")
   elif bmi <25 or bmi <30:
       print("You are overweight")
   else:
       print("You have obese")
   return bmi


def multi():
    x = float(input('Enter a number:'))
    y = float(input('Enter a second number:'))
    z = print(x*y)
    return z


def factorial():
    import math
    x = int(input("Enter a number to find its factorial:"))
    f = math.factorial(x)
    print("The factorial of:", x , " is :", f)
    return f
    
def exPower():
    x = int(input("Enter a number:"))
    y = int(input("Enter the exponential value:"))
    z = x**y
    print("Exponential value:", z)
    return z



def options():
 print("1---> Order tickets")  
 print("2---> Calculate BMI ")
 print("3---> Multiply two numbers")
 print("4---> Find the factorial of a value")
 print("5---> Find the exponential value of a number")
 print("6---> Exit")
 
 
main() 
  
    