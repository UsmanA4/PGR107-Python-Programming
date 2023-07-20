# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 14:42:04 2023

@author: Usman Ahmad
"""

import options
choice =int(input('Type a number (0 for exit):'))

while choice !=0:
    if choice ==1:
        f1=input('Type in your food item 1:')
        f2=input('Type in your food item 2:')
        f3=input('Type in your food item 3:')
        
        f = [f1,f2,f3]
        print('Your items are shown below\n:',f)
        options.options()
        choice =int(input('Type a number (0 for exit):'))
    if choice ==2:
        g1 = input('Type in your first game:')
        g2 = input('Type in your second game:')
        g3 = input('Type in your third game:')
        f = [g1,g2,g3]
        if "PS4" in g1 and "PS4" in g2 and "PS4" in g3 :
            print(f)
        if "PS4" not in g1:
         print('Invalid Input! this is not a PS4 game:',g1 )   
         
        if "PS4" not in g2:
          print('Invalid Input! this is not a PS4 game:',g2)
        if "PS4" not in g3:
           print('Invalid Input! this is not a PS4 game:',g3)
        else:
         options.options()
         choice =int(input('Type a number (0 for exit):'))   
        
    if choice ==3:
     account =25000
     item1 =input('Type in your first clothing item:')
     price =int(input('How much does your clothes cost?'))
     
     item2 =input('Type in your second clothing item:')
     price2=int(input('How much does your clothes cost?'))
     item3 =input('Type in your third clothing item:')
     price3=int(input('How much does your clothes cost?'))
     
     i = [item1,item2,item3]
     
     left= account-price-price2-price3      
     
     print('Your items:', i)
     print('Your account balance before the shopping: ' , account , ' after the shopping:', left)       
    options.options()      
    choice =int(input('Type a number (0 for exit):'))   
         
        