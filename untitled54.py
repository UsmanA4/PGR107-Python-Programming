# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 11:08:33 2023

@author: Usman Ahmad
"""

l1 = []
l1.append(1)
l1.append(2)
l1.append(3)
l1.append(4)
l1.append(5)
l1.append(6)
l1.append(7)

x = int(input("Search for a number:"))
if x in l1:
    print("Results found:",x , " in position:", l1.index(x))
else:
 print("No results found!!")     