# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 13:13:43 2023

@author: Usman Ahmad
"""

MAX_BOTTLES=21
numberofbottles=int(input("Hvor mange flasker trenger du?"))

if numberofbottles < MAX_BOTTLES:
 MAX_BOTTLES=MAX_BOTTLES-numberofbottles
 print("Du tok :", numberofbottles , "Det er :" , MAX_BOTTLES, ", igjen")
 
 mer = input("Vil du ta ut flere flasker?")
 if mer == "ja":
     take = int(input("Hvor mange flasker vil du ta ut nå!"))
     if take <MAX_BOTTLES:
         MAX_BOTTLES = MAX_BOTTLES-take
         print("Du tok :", take , "til ,Det er :" , MAX_BOTTLES, ", igjen")
     else:
         print("Det er ikke mulig å ta ut så mange flasker")
else:
     print("Det er ikke så mange flasker på lager")