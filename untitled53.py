# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 10:52:00 2023

@author: Usman Ahmad
"""
print("Enter words to append:")
values = []
userInput = input("")

while userInput.upper() !="Q":
 values.append(userInput)
 userInput=input("")
 if userInput.upper() =="Q":
      print(values)
      