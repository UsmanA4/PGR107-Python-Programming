# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 08:50:32 2023

@author: Usman Ahmad
"""

list1 = [1,2,3,4,5,6,7,8,9]
list1.append(654)
list1.append(7612)    
x = int(input("Search for a number:"))
if x in list1:
  print("Results found:",x , " at index:", list1.index(x))  
else:
 print("Invalid input, no results found!")    
 
 
i = int(input("display a value:"))
list2 = [1,2,3,4,5,6,7]
print(list2.pop(i)) 

list3 = [1,2,3,4,5,6,90,130]
print(list3)
r = int(input('Remove a value:'))
list3.remove(r)
print(list3)
a = int(input("Append a value:"))
list3.append(a)
print(list3)
 


 
