# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 11:56:10 2023

@author: Usman Ahmad
"""

class bug: #Vår bug klasse
    
    def __init__(self, initialPosition): #definerer init klassen og variabler
        self.bugPosition = initialPosition #Bruker self til å definere selve posisjonen
        self.bugDirection = 1 #beveger buggen mot høyre
        
        
    def turnRight(self): #Metoden som beveger den tilbake mot høyre ved retningsskifte
        self.bugDirection = 1
        return print("Endrer retning mot høyre")
        
    def turnLeft (self): #Bevege buggen mot venstre
        self.bugDirection = -1
        return print("Bytter retning mot venstre")#bevege buggen i andre vei
        
    def move(self): #Beveger buggen videre i nåværende retning
        self.bugPosition += self.bugDirection #bevege den videere i pågående retning
        return print("Beveger oss i nåværende retning")
        
    def getPosition(self): #Henter den aktuelle posisjonen til buggen
        return print("Nåværende posisjon:",self.bugPosition) #gir oss nåværende posisjon på buggen
        
bugsy = bug(10)
    
bugsy.move()
bugsy.move()
bugsy.move() 
bugsy.turnLeft()
bugsy.move()
bugsy.move()
bugsy.turnRight()
bugsy.move()


bugsy.getPosition()
print("Forventet posisjon 12:") #