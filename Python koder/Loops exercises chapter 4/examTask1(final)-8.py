#-*- coding: utf-8 -*-
"""
Created on Sun Apr 23 09:13:46 2023

@author: .....
"""



#Created a function removeSensitiveWord using arguments as filenames to perform the operation
#o_File = Original text file.
#s_File = Sensitive wordlist. 
#e_file = Edited text after the removal of sensitive word(s).

import os
def removeSensitiveWords(o_File , s_File , e_File):

#Initializing variables for the filepath and use this to display the filename   
 o_path = './Python Exam 2023/'+o_File  #filepath and name to o_File 
 o_filename = os.path.basename(o_path)
 
 s_path ='./Python Exam 2023/'+s_File #filepath and name to s_File
 s_filename = os.path.basename(s_path)
 
 e_path ='./Python Exam 2023/'+e_File #filepath and name to e_File
 e_filename = os.path.basename(e_path)
 
 
#Reading the original file.
 
 try:
     of = open(o_File , 'r')
     original_word = of.read()
          
 except IOError:
     return  print("Error! File:" ,"'", o_filename,"'"," doesn't exist!")
 
#Reading the list of sensitive words     
 try:
     sf = open(s_File , 'r')
     wordsInText =sf.read()
     
     #Splits the lines into individual words in text:
     sensitive_wordlist = wordsInText.split()  
         
 except IOError:
      return print("Error! File:" ,"'", s_filename,"'"," doesn't exist!")
 
#Replace the sensitive words with asteriks "*" in the list.
 try:
  rep_word = original_word
  for sensitive_word in sensitive_wordlist:
     
     
     if sensitive_word in sensitive_wordlist: #replaces lowercase words only. 
      asterisk = '*' * len(sensitive_word)     
      rep_word = rep_word.replace(sensitive_word , asterisk) 
     elif sensitive_word in sensitive_wordlist[0].upper: #Replaces the word if the letter is in uppercase
         rep_word = rep_word.replace(sensitive_word , asterisk)
      
     if sensitive_word not in sensitive_wordlist:
         print("Sensitive word was not found in the  list :(")
         
 
#Writes the changes out to the new file.

  ef = open(e_File, 'w') 
  ef.write(rep_word)   
  
 except FileNotFoundError:
     return print("Error! File:" ,"'", e_filename,"'"," doesn't exist!")
 
 print("Senstive word(s) was successfully removed and the new changes is saved to file:" , e_filename)  
removeSensitiveWords('censoredText.txt','sensitiveWordlist.txt','sensitiveeed.txt')  



