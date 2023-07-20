# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 09:13:46 2023

@author: Usman Ahmad
"""

#Created a function removeSensitiveWord using arguments as filenames to perform the operation
#o_File = Original text file.
#s_File = Sensitive wordlist. 
#e_file = Edited text after the removal of sensitive word(s).
import os
def removeSensitiveWords(o_File , s_File , e_File):

#Initializing variables for the filepath and use this to display the filename   
 o_path = './Python koder 2023/'+o_File  #filepath to o_File
 o_filename = os.path.basename(o_path)
 
 s_path ='./Python koder 2023/'+s_File #filepath to s_File
 s_filename = os.path.basename(s_path)
 
 e_path ='./Python koder 2023/'+e_File #filepath to e_File
 e_filename = os.path.basename(e_path)
 
#Reading the original file.
 
 try:
     of = open(o_File , 'r')
     original_word = of.read()
          
 except FileNotFoundError:
     return  print("Error! File:" ,"'", o_filename,"'"," doesn't exist!")
 
#Reading the list of sensitive words     
 try:
     sf = open(s_File , 'r')
     
     textInList =sf.read()
     
     sensitive_wordlist = textInList.split() #splits the text into individual words.
         
 except FileNotFoundError:
      return print("Error! File:" ,"'", s_filename,"'"," doesn't exist!")
 
#Replace the sensitive words with asteriks "*" in the list.
 rep_word = original_word
 for sensitive_word in sensitive_wordlist:
     
     if sensitive_word in sensitive_wordlist:    
      asterisk = '*' * len(sensitive_word)
      rep_word = rep_word.replace(sensitive_word , asterisk) #replaces sensitive words with asterisk
      
     else:
         print("Sensitive word was not found in the  list :(")
         
 
#Write the changes out to the new file.
 try:
    ef = open(e_File, 'w') 
    ef.write(rep_word)
 except FileNotFoundError:
     return print("Error! File:" ,"'", e_filename,"'"," doesn't exist!")
 

     
 print("Senstive word(s) was successfully removed and new changes saved to file:" , e_filename)
removeSensitiveWords('censored2.txt','sensitive2.txt','newsense2.txt')  



