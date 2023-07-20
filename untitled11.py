# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 08:54:13 2023

@author: Usman Ahmad
"""

def eksamen(karakter):
    
 if karakter =="A":
   print("Du er mashallah en flink  kar , fortsett slik!")

 elif karakter == "B":
       print("Very good my man , neste gang !")
       
 elif karakter == "C":
       print("Nice , inshallah du klarer det neste gang :)")
       x= input("Hva er årsaken til karakteren?")
       if x =="øvde ikke" or x =="vetikke":
        print("Dette er ikke en gyldig grunn")    
 elif karakter == "D":
        print("Nice , prøv hardere neste gang")
        
 elif karakter == "E":
        print("Nice , inshallah du klarer det neste gang :)")
 elif karakter == "F":
         print("Du bør krige for å nå ambisjonene dine")         

 else:
   print("Dette er ikke en karakter !!!")    
   
   
eksamen(input("Skriv en karakter:"))               