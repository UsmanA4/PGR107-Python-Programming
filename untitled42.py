# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 18:16:46 2023

@author: Usman Ahmad
"""
count=1
f = open("task2.txt", "r")
for i in f:
    print(count,":",i)
    count=count+1

