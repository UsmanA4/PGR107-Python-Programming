# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 18:33:39 2023

@author: Usman Ahmad
"""

points =0
wrong=0
q = ["Q1)What is the capital of Norway?", "Q2)What is the currency of Norway? ", "Q3)What is the largest city in Norway? ", "Q4)When is constitution day (the national day) of Norway? ", "Q5)What color is the background of the Norwegian flag?", "Q6)How many countries does Norway border? ",
     "Q7)What is the name of the university in Trondheim? ", "Q8)How long is the border between Norway and Russia? ", "Q9)Where in Norway is Stavanger? ", "Q10)From which Norwegian city did the world’s famous composer Edvard Grieg come? "]
#-------q5 unde
print(q[4])
q5o = ["a.Red", "b.White", "c.Blue", "d.Yellow"]

for i in q5o:
     print(i)
     
a1 = input("Your answer:")
if a1 =="a":
    print("Riktig")
    points=points+1
    print("Dine poeng:",points)
    #-------q6 starts here
    print(q[5])
    q6o = ["a.1", "b.2", "c.3", "d.4"]
    
    for i in q6o:
         print(i)
         
    a1 = input("Your answer:")
    if a1 in q6o[2]:
        print("Riktig")
        points=points+1
        print("Dine poeng:",points)
        
        #-------------------- place q7-10 here
        print(q[6])
        q7o = ["a.UiS", "b.UiO", "c.NMBU", "d.NTNU"]

        for i in q7o:
             print(i)
             
        a1 = input("Your answer:")
        if a1 in q7o[3]: #-------q7 under
            print("Riktig")
            points=points+1
            print("Dine poeng:",points)
            # q8 under-----------------------------------
            print(q[7])
            q8o = ["a.96 km", "b.196 km", "c.296 km", "d.396 km"]
            for j in q8o:
                print(j)
            
            a1 = input("Your answer:")
            if a1 in q8o[1]:
                print("Riktig")
                points=points+1
                print("Dine poeng:",points)
                #-----------------q9 starts here
                print(q[8])
                q9o = ["a.North", "b.South", "c.South-west", "d.South-east"]
                for k in q9o:
                  print(k)
                a1 = input("Your answer:")
                if a1 in q9o[2]:
                    print("Riktig")
                    points=points+1
                    print("Dine poeng:",points)
                    #-----------------q10 starts here
                    print(q[9])
                    q10o = ["a.Oslo", "b.Bergen", "c.Stavanger", "d.Tromsø"]
                    for l in q10o:
                      print(l)
                    a1 = input("Your answer:")
                    if a1 in q10o[1]:
                        print("Riktig")
                        points=points+1
                        print("Dine poeng:",points)
                    else:
                        print("Feil!!")

                        print("Dine poeng:",points)
                        print("Feil", wrong)
                        
                    
                #-------------------- q10 ends here
            else:
                print("Feil!!")

                print("Dine poeng:",points)
                print("Feil", wrong)
                print(q[8])
                q9o = ["a.North", "b.South", "c.South-west", "d.South-east"]
                for k in q9o:
                  print(k)
                a1 = input("Your answer:")
                if a1 in q9o[2]:
                    print("Riktig")
                    points=points+1
                    print("Dine poeng:",points)
                   
                    
                #-------------------- q9 ends here
            #-------------------- q8 ends here
            
            
        else: # this else statement belongs to q7
            print("Feil!!")
            print("Dine poeng:",points)
            print("Feil",wrong )
            # q8 under-----------------------------------
            print(q[7])
            q8o = ["a.96 km", "b.196 km", "c.296 km", "d.396 km"]
            for j in q8o:
                print(j)
            a1 = input("Your answer:")
            if a1 in q8o[1]:
                print("Riktig")
                points=points+1
                print("poeng:",points)
                
                #-----------------q9 starts here
                print(q[8])
                q9o = ["a.North", "b.South", "c.South-west", "d.South-east"]
                for k in q9o:
                  print(k)
                a1 = input("Your answer:")
                if a1 in q9o[2]:
                    print("Riktig")
                    points=points+1 
                    print("Dine poeng:",points)
                    #-----------------q10 starts here
                    print(q[9])
                    q10o = ["a.Oslo", "b.Bergen", "c.Stavanger", "d.Tromsø"]
                    for l in q10o:
                      print(l)
                    a1 = input("Your answer:")
                    if a1 in q10o[1]:
                        print("Riktig")
                        points=points+1
                        print("Dine poeng:",points)
                    else:
                        print("Feil!!")

                        print("Dine poeng:",points)
                        print("Feil", wrong)
                        
                    
                #-------------------- q10 ends here 
                   
                #-------------------- q9 ends here
                
            else:
                print("Feil!!")

                print("Dine poeng:",points)
                print("Feil", wrong)
                
                #-----------------q9 starts here
                print(q[8])
                q9o = ["a.North", "b.South", "c.South-west", "d.South-east"]
                for k in q9o:
                  print(k)
                a1 = input("Your answer:")
                if a1 in q9o[2]:
                    print("Riktig")
                    points=points+1
                    print("Dine poeng:",points)
                else:
                    #-----------------q10 starts here
                    print(q[9])
                    q10o = ["a.Oslo", "b.Bergen", "c.Stavanger", "d.Tromsø"]
                    for l in q10o:
                      print(l)
                    a1 = input("Your answer:")
                    if a1 in q10o[1]:
                        print("Riktig")
                        points=points+1
                        print("Dine poeng:",points)
                    else:
                        print("Feil!!")

                        print("Dine poeng:",points)
                        print("Feil", wrong)
                        
                    
                #-------------------- q10 ends here
                    
                #-------------------- q9 ends here
               
                
            #-------------------- q8 ends here
        
    else:
     print("Feil!!")
     print("Dine poeng:",points)
     print("Feil", wrong)    
     #-------------------- place q7-10 here

     print(q[6])
     q7o = ["a.UiS", "b.UiO", "c.NMBU", "d.NTNU"]

     for i in q7o:
          print(i)
          
     a1 = input("Your answer:")
     if a1 in q7o[3]: #-------q7 under
         print("Riktig")
         points=points+1
         print("Dine poeng:",points)
         # q8 under-----------------------------------
         print(q[7])
         q8o = ["a.96 km", "b.196 km", "c.296 km", "d.396 km"]
         for j in q8o:
             print(j)
         
         a1 = input("Your answer:")
         if a1 in q8o[1]:
             print("Riktig")
             points=points+1
             print("Dine poeng:",points)
             #-----------------q9 starts here
             print(q[8])
             q9o = ["a.North", "b.South", "c.South-west", "d.South-east"]
             for k in q9o:
               print(k)
             a1 = input("Your answer:")
             if a1 in q9o[2]:
                 print("Riktig")
                 points=points+1
                 print("Dine poeng:",points)
                 #-----------------q10 starts here
                 print(q[9])
                 q10o = ["a.Oslo", "b.Bergen", "c.Stavanger", "d.Tromsø"]
                 for l in q10o:
                   print(l)
                 a1 = input("Your answer:")
                 if a1 in q10o[1]:
                     print("Riktig")
                     points=points+1
                     print("Dine poeng:",points)
                 else:
                     print("Feil!!")

                     print("Dine poeng:",points)
                     print("Feil", wrong)
                     
                 
             #-------------------- q10 ends here
         else:
             print("Feil!!")

             print("Dine poeng:",points)
             print("Feil", wrong)
             print(q[8])
             q9o = ["a.North", "b.South", "c.South-west", "d.South-east"]
             for k in q9o:
               print(k)
             a1 = input("Your answer:")
             if a1 in q9o[2]:
                 print("Riktig")
                 points=points+1
                 print("Dine poeng:",points)
                 #-----------------q10 starts here
                 print(q[9])
                 q10o = ["a.Oslo", "b.Bergen", "c.Stavanger", "d.Tromsø"]
                 for l in q10o:
                   print(l)
                 a1 = input("Your answer:")
                 if a1 in q10o[2]:
                     print("Riktig")
                     points=points+1
                     print("Dine poeng:",points)
                 else:
                     print("Feil!!")

                     print("Dine poeng:",points)
                     print("Feil", wrong)
                     
                 
             #-------------------- q10 ends here   
                
                 
             #-------------------- q9 ends here
         #-------------------- q8 ends here
         
         
     else: # this else statement belongs to q7
         print("Feil!!")
         print("Dine poeng:",points)
         print("Feil",wrong )
         # q8 under-----------------------------------
         print(q[7])
         q8o = ["a.96 km", "b.196 km", "c.296 km", "d.396 km"]
         for j in q8o:
             print(j)
         a1 = input("Your answer:")
         if a1 in q8o[1]:
             print("Riktig")
             points=points+1
             print("poeng:",points)
             
             #-----------------q9 starts here
             print(q[8])
             q9o = ["a.North", "b.South", "c.South-west", "d.South-east"]
             for k in q9o:
               print(k)
             a1 = input("Your answer:")
             if a1 in q9o[2]:
                 print("Riktig")
                 points=points+1
                 print("Dine poeng:",points)
                
             #-------------------- q9 ends here
             
         else:
             print("Feil!!")

             print("Dine poeng:",points)
             print("Feil", wrong)
             
             #-----------------q9 starts here
             print(q[8])
             q9o = ["a.North", "b.South", "c.South-west", "d.South-east"]
             for k in q9o:
               print(k)
             a1 = input("Your answer:")
             if a1 in q9o[2]:
                 print("Riktig")
                 points=points+1
                 print("Dine poeng:",points)
             else:
                 #-----------------q10 starts here
                 print(q[9])
                 q10o = ["a.Oslo", "b.Bergen", "c.Stavanger", "d.Tromsø"]
                 for l in q10o:
                   print(l)
                 a1 = input("Your answer:")
                 if a1 in q10o[1]:
                     print("Riktig")
                     points=points+1
                     print("Dine poeng:",points)
                 else:
                     print("Feil!!")

                     print("Dine poeng:",points)
                     print("Feil", wrong)
                     
                 
             #-------------------- q10 ends here
                 
             #-------------------- q9 ends here
            
             
         #-------------------- q8 ends here
     
     #----------------------q5 ends here
    
else:
 print("Feil!!")
 print("Dine poeng:",points)
 print("Feil", wrong)    
 #-------q6 starts here
 print(q[5])
 q6o = ["a.1", "b.2", "c.3", "d.4"]

 for i in q6o:
      print(i)
      
 a1 = input("Your answer:")
 if a1 in q6o[2]:
     print("Riktig")
     points=points+1
     print("Dine poeng:",points)
     

     
     
 else:
  print("Feil!!")
  print("Dine poeng:",points)
  print("Feil", wrong)    
  print(q[6])
  q7o = ["a.UiS", "b.UiO", "c.NMBU", "d.NTNU"]

  for i in q7o:
       print(i)
       
  a1 = input("Your answer:")
  if a1 in q7o[3]: #-------q7 under
      print("Riktig")
      points=points+1
      print("Dine poeng:",points)
      # q8 under-----------------------------------
      print(q[7])
      q8o = ["a.96 km", "b.196 km", "c.296 km", "d.396 km"]
      for j in q8o:
          print(j)
      
      a1 = input("Your answer:")
      if a1 in q8o[1]:
          print("Riktig")
          points=points+1
          print("Dine poeng:",points)
          #-----------------q9 starts here
          print(q[8])
          q9o = ["a.North", "b.South", "c.South-west", "d.South-east"]
          for k in q9o:
            print(k)
          a1 = input("Your answer:")
          if a1 in q9o[2]:
              print("Riktig")
              points=points+1
              print("Dine poeng:",points)
              #-----------------q10 starts here
              print(q[9])
              q10o = ["a.Oslo", "b.Bergen", "c.Stavanger", "d.Tromsø"]
              for l in q10o:
                print(l)
              a1 = input("Your answer:")
              if a1 in q10o[2]:
                  print("Riktig")
                  points=points+1
                  print("Dine poeng:",points)
              else:
                  print("Feil!!")

                  print("Dine poeng:",points)
                  print("Feil", wrong)
                  
              
          #-------------------- q10 ends here
      else:
          print("Feil!!")

          print("Dine poeng:",points)
          print("Feil", wrong)
          print(q[8])
          q9o = ["a.North", "b.South", "c.South-west", "d.South-east"]
          for k in q9o:
            print(k)
          a1 = input("Your answer:")
          if a1 in q9o[2]:
              print("Riktig")
              points=points+1
              print("Dine poeng:",points)
             
          #-------------------- q9 ends here
      #-------------------- q8 ends here
      
      
  else: # this else statement belongs to q7
      print("Feil!!")
      print("Dine poeng:",points)
      print("Feil",wrong )
      # q8 under-----------------------------------
      print(q[7])
      q8o = ["a.96 km", "b.196 km", "c.296 km", "d.396 km"]
      for j in q8o:
          print(j)
      a1 = input("Your answer:")
      if a1 in q8o[1]:
          print("Riktig")
          points=points+1
          print("poeng:",points)
          
          #-----------------q9 starts here
          print(q[8])
          q9o = ["a.North", "b.South", "c.South-west", "d.South-east"]
          for k in q9o:
            print(k)
          a1 = input("Your answer:")
          if a1 in q9o[2]:
              print("Riktig")
              points=points+1
              print("Dine poeng:",points)
             
          #-------------------- q9 ends here
          
      else:
          print("Feil!!")

          print("Dine poeng:",points)
          print("Feil", wrong)
          
          #-----------------q9 starts here
          print(q[8])
          q9o = ["a.North", "b.South", "c.South-west", "d.South-east"]
          for k in q9o:
            print(k)
          a1 = input("Your answer:")
          if a1 in q9o[2]:
              print("Riktig")
              points=points+1
              print("Dine poeng:",points)
              #-----------------q10 starts here
              print(q[9])
              q10o = ["a.Oslo", "b.Bergen", "c.Stavanger", "d.Tromsø"]
              for l in q10o:
                print(l)
              a1 = input("Your answer:")
              if a1 in q10o[1]:
                  print("Riktig")
                  points=points+1
                  print("Dine poeng:",points)
              else:
                  print("Feil!!")

                  print("Dine poeng:",points)
                  print("Feil", wrong)
                  
              
          #-------------------- q10 ends here   
              
          else:
              #-----------------q10 starts here
              print(q[9])
              q10o = ["a.Oslo", "b.Bergen", "c.Stavanger", "d.Tromsø"]
              for l in q10o:
                print(l)
              a1 = input("Your answer:")
              if a1 in q10o[1]:
                  print("Riktig")
                  points=points+1
                  print("Dine poeng:",points)
              else:
                  print("Feil!!")

                  print("Dine poeng:",points)
                  print("Feil", wrong)
                  
                  
              
          #-------------------- q10 ends here
              
          #-------------------- q9 ends here
         
          
      #-------------------- q8 ends here
  #----------------------q6 ends here
  #-------------------- place q7-10 under:
      
 #----------------------q5 ends here
 