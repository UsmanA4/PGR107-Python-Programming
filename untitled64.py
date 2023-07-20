# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 19:07:22 2023

@author: Usman Ahmad
"""

def main():
 usr =""
 pswd=""
 r_user = ["PGR107"]
 r_pass = ["Python"]
 q = ["What is the capital of Norway?" , "What is the currency of Norway? " , "What is the largest city in Norway? " , "When is constitution day (the national day) of Norway? " 
      , "What color is the background of the Norwegian flag?" , "How many countries does Norway border? " , "What is the name of the university in Trondheim? " , "How long is the border between Norway and Russia? "  
       ,"Where in Norway is Stavanger? " , "From which Norwegian city did the world’s famous composer Edvard Grieg come? "]

 while (usr !="PGR107" and r_pass !="Python"):
     
    usr = input("Enter username:")
    pswd = input("Enter password:")
    if(usr ==r_user[0] and pswd ==r_pass[0]):
        print(q[0])
        q1()

    
    

def q1():
 q = ["Q1)What is the capital of Norway?" , "Q2)What is the currency of Norway? " , "Q3)What is the largest city in Norway? " , "Q4)When is constitution day (the national day) of Norway? " 
       , "Q5)What color is the background of the Norwegian flag?" , "Q6)How many countries does Norway border? " , "Q7)What is the name of the university in Trondheim? " , "Q8)How long is the border between Norway and Russia? "  
        ,"Q9)Where in Norway is Stavanger? " , "Q10)From which Norwegian city did the world’s famous composer Edvard Grieg come? "]  
   
 points =0
 wrong_answ = 0
 q1o = ["a. Bergen", "b. Oslo" , "c. Stavanger" , "d. Trondheim"] 


 for i in q1o:  #printer ut spm 1 
    print(i)
 a1 = input("Your answer:")
 if a1 in q1o[1]:
  print("Riktig")
  points = points+1

  print("Dine poeng:",points)
  print(q[1])
  q2o = ["a.Euro " , "b.Pound" , "c.Krone" , "d.Deutsche Mark "] #lagrer svarene i en liste!


  for i in q2o: #printer utt spm 2
     print("\n"+i)
  a1 = input("Your answer:")
  if a1 in q2o[2]:
   points = points +1
   print("Riktig")
   print("Dine poeng:", points)
   print(q[2])

  else:
     print("Feil!!") #printer utt spm 2
     wrong_answ =wrong_answ+1
     #print("Dine poeng:",points)
     print("Feil", wrong_answ)
     print(q[2])
     for i in q2o:
        print(i)
     a1 = input("Your answer:")
     if a1 in q2o[2]:
      print("Riktig")
      print("Dine poeng:", points)
      print(q[2])
  
 else:
    print("Feil!!")
    points =0
    print("Dine poeng:", points)
    
    print(q[1])
    q2o = ["a.Euro " , "b.Pound" , "c.Krone" , "d.Deutsche Mark "] #lagrer svarene i en liste!


    for i in q2o: 
       print("\n"+i)
    a1 = input("Your answer:")
    if a1 in q2o[2]:
     print("Riktig")
     print("Dine poeng:",score(0))
     print(q[2])

    else:
       print("Feil!!")
       wrong_answ =wrong_answ+1
       #print("Dine poeng:",points)
       print("Feil", wrong_answ)
       print(q[2])
 
def score(p=0):
    po =p
    po=po+1
    print(po)
    return po
main()             
       