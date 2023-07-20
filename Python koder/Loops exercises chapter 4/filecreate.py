# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 11:01:21 2023

@author: Usman Ahmad
"""
f = open("best.txt","w")
x = input("Skriv en setning:")
y = input("Skriv enda en sentning")
f.write(x)
f.write("\n"+y)

f.close()