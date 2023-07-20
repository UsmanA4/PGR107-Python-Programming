# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 08:30:48 2023

@author: Usman Ahmad
"""

print("Fotball quiz 2023")

x=""
points=1

name =input("Hva heter du?")
while x !=39:
    x=int(input("Hvor gammel er ronaldo?"))
if x==39:
    y=input("Rødt kort at spilleren er diskvalifisert ? (Ja/Nei)")
    points = points +1 
if y=="ja":
    points = points +1 
    z=input("Hva er det fulle navnet til Pogba?")
    z=z.upper()
    if z=="PAUL POGBA":
        g =input("Hvilket lag spiller ronaldo for nå?")
        g = g.upper()
        if g=="AL NASSR":
            points=points +1 
            print("Gratulerer:", name, " !Du har fått" , points , "av 4 poeng!!!" )
        else:
         print("Du svarte dessverre feil!")
         print("Dine poeng:", points)
            
    else:
        print("Du svarte feil!!")
        print("Dine poeng:", points-1)
  
else:
    print("Du tapte!!")   
    print("Dine poeng:", points-1)     