# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 10:01:35 2023

@author: Usman Ahmad
"""
  
print("Hva vil du gjøre?")
x= ["1:Lage en txt fil", "2:Lese av en fil" , "3:Svare på noen spørsmål"  ]


for z in x :
    print(z)

x = int(input(""))
if x ==1:
    print("Lag din fil:")
    name= input("Hva skal filen hete?")
    st = input("Skriv en setning:")
    d = open(name+".txt","w")
    d.write(st)
    se = input("Vil du skrive en til setning?")
    if se=="ja":
        sd= input("Skriv en setning:")
        d.write("\n"+sd)
        d.close()
    else:
        d.close()
        
elif x ==2:
  r1 = input("Skriv filnavnet du vil lese av?")  
  r2 = open(r1+".txt", "r")      
  print(r2.read())
elif x==3 :
    print("Under production")