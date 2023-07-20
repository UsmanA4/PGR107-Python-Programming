# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 13:03:34 2023

@author: ....
"""

class bug:
    def __init__(self, initialPosition): #definerer init klassen og variabler
        self.bugDirection = initialPosition #Bruker self til å definere selve posisjonen
        self.bugDir = self.bugDirection #beveger buggen mot høyre
        self.bugDir=1
        
        
        
    def turnRight(self): #Metoden som beveger den tilbake mot høyre ved retningsskifte
    
        
        self.bugDir= 1
        
        
    def turnLeft(self): #Bevege buggen mot venstre
      
        self.bugDir = -1
        
    def move(self): #Beveger buggen videre i nåværende retning
      
        self.bugDirection +=self.bugDir
        
    def getCurrentPosition(self): #Henter den aktuelle posisjonen til buggen
       return print("Dette er nåværende posisjon" ,self.bugDirection) #gir oss nåværende posisjon på buggen
   
#Tester buggen og beveger den
bugsy = bug(10)

bugsy.turnLeft() #Endrer retning mot venstre
bugsy.move() #Buggen beveger seg mot plass 9
bugsy.move() #Buggen beveger seg mot plass 8
bugsy.turnRight() #Endrer retning mot høyre
bugsy.move() #Buggen beveger seg mot plass 9
print("Forventet posisjon: 9")
bugsy.getCurrentPosition() #Den faktiske posisjonen



        
        

