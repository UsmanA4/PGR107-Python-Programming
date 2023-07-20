# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 16:50:20 2023

@author: Usman Ahmad
"""
count =0
sum =0
num =1
fn =input('')
ln =input('')
while num !=-1:
 num = int(input(""))
 sum = sum + num
 count += 1

if count ==0:
  print('')

if num ==-1:
    c = count-1
    avg =sum/c
    print(avg)

    