# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 10:28:14 2023

@author: Usman Ahmad
"""
print("Enter numbers to append in the list (Q for exit):")
values = []
userInput = input("")
while userInput.upper() !="Q":
    values.append(userInput)
    userInput=input("")
    if userInput.upper() == "Q":
        print(values)
        break