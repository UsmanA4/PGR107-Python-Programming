# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 17:33:53 2023

@author: Usman Ahmad
"""
konto=97000
password=''
while password !='teslaisthebest':
 password=input("Hva er passordet til facebook-brukeren til musk?")
 
 if password =="teslaisthebest":
  take=input("Hei Mr Musk! Vil du ta ut penger?")
  if take=="ja":
    much= int(input("Hvor mye vil du ta ut?"))
    if much<konto:
        konto = konto - much
        
        print("din saldo er nå:" , konto)
        print(" Nettbanken avslutter........")
  
    else:
        print("Det er ikke mulig å ta ut så mye!!")
  else:
        print("Ok ha en fin dag")
        print("Din  saldo er :" , konto)
   
 