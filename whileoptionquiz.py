# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 09:30:58 2023

@author: Usman Ahmad
"""
import options2
choice = int(input('Enter a number (0 for exit):'))

while choice !=0:
    if choice ==1:
     num1 = int(input('Enter a number:'))
     num2 = int(input('Enter the second number:'))
     sum = num1+num2
     n=1
     n=n+1
     avg = sum/n
     ma = max(num1, num2)
     mi = min(num1, num2)
     print('Sum:', sum)
     print('Average:', avg)
     print('Max:', ma)
     print('Min:', mi)
     options2.options()
     choice = int(input('Enter a number (0  for exit):'))
    
    elif choice ==2:
        n1 = int(input('Enter a number 1:'))
        n2 = int(input('Enter a number 2:'))
        add = n1+n2
        sub = n1-n2
        dev = n1/n2
        mul= n1*n2
        print("Addition:",add)
        print('Substraction:',sub)
        print('Devide:',dev)
        print('Multiplication:', mul)
        options2.options()
        choice = int(input('Enter a number (0  for exit):'))
        
    elif choice ==3:
        points=0
        name = input('Type in your name:')
        q1 = input('What is name of the largest building in the world?:')
        if q1=="burj khalifa":
            points =points+1
            print('Well done you got:',points , ' out of 6 points' )
            q2 = input('What is the capital of Pakistan?:')
            if q2=="islamabad":
                points =points+1
                print('Well done you got:',points , ' out of 6 points' )
                q3 = input('What is the name of the hightest grossing MCU movie?:')
                if "endgame" in q3 :
                    points =points+1
                    print('Well done you got:',points , ' out of 6 points')
                    q4 =input('The logo for luxury car maker Porsche features which animal?:')
                    if q4 =="horse":
                      points =points+1
                      print('Well done you got:',points , ' out of 6 points' )
                      q5 = input('Rojo is the Spanish word for which colour?:')
                      if q5=="red":
                       points =points+1
                       print('Well done you got:',points , ' out of 6 points' ) 
                       q6 =input('What is the name of Kratoss son?:')
                       if q6 =="atreus":
                         points =points+1
                         print('Congratulations:',name ,'! you got:',points , ' out of 6 points' )
                         print("Type 3 if you want to retake the quiz :)")
                         options2.options()
                         choice = int(input('Enter a number (0  for exit):'))
                       else:
                           print('Sorry wrong answer! Your total score is:', points)
                           options2.options()
                           choice = int(input('Enter a number (0  for exit):'))
                      else:
                       print('Sorry wrong answer! Your total score is:', points)
                       options2.options()
                       choice = int(input('Enter a number (0  for exit):'))
                    else:
                        print('Sorry wrong answer! Your total score is:', points)
                        options2.options()
                        choice = int(input('Enter a number (0  for exit):'))
                        
                        
                else:
                    print('Sorry wrong answer! Your total score is:', points)
                    options2.options()
                    choice = int(input('Enter a number (0  for exit):'))
            else:
                print('Sorry wrong answer! Your total score is:', points)
                options2.options()
                choice = int(input('Enter a number (0  for exit):'))
        else:
            print('Sorry! wrong answer , wanna try again type 3')
            options2.options()
            choice = int(input('Enter a number (0  for exit):'))