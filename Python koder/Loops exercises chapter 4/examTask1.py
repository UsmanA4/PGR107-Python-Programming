# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 09:13:46 2023

@author: Usman Ahmad
"""

#Created a function  to perform the operation

def editCensored_list(o_File , s_File , e_File):
 
    
 #Reading the original file
 
 try:
     of = open(o_File , 'r')
     o_words = of.read()
          
 except FileNotFoundError:
     return  print("File  {o_File} doesn't exist")
 
# Read the list of sensitive words     
 try:
     sf = open(s_File , 'r')
     sensitive_wordlist = sf.read().split() #splits the text into individual words
         
 except FileNotFoundError:
      return print("File {s_File} doesn't exist")
 
 # Replace the sensitive words with asteriks "*" in the list.
 rep_word = o_words
 for sensitive_word in sensitive_wordlist:
     
     if sensitive_word in sensitive_wordlist:    
      asteriks = '*' * len(sensitive_word)
      rep_word = rep_word.replace(sensitive_word , asteriks)
      
     else:
         print("Sensitive word was not found  in the  list :(")
         
 
 # Write the changes out to the new file
 try:
    ef = open(e_File, 'w') 
    ef.write(rep_word)
 except FileNotFoundError:
     return print("File  {e_File} doesn't exist")
     
 try:
  editCensored_list('censored2.txt','sensitive2.txt','newsense2.txt')    
  print("Text was successfully edited and saved to {e_File}")
 
 except IOError :
    return print("Error! Something went wrong when replacing the sensitive word/s from the text , please try again! ")
