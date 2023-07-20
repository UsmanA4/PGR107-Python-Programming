# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 08:59:19 2023

@author: ....
"""

# Function to check if a string is a palindrome
def palindrome_checker(s):
    s = s.lower()  # Make the string lowercase
    return s == s[::-1]  # Compare the original string to the reversed string

# Get user input
user_input = input("Please enter a string: ")

# Check if the input is a palindrome using the palindrome_checker function
if palindrome_checker(user_input):
    print(user_input, "is a palindrome.")
else:
    print(user_input, "is not a palindrome.")
