# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 10:03:13 2023

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


 for i in q1o:
    print(i)
 a1 = input("Your answer:")
 if a1 in q1o[1]:
  print("Riktig")
  print("Dine poeng:",score(0))
  print(q[1])
  q2( )
 else:
    print("Feil!!")
    points =0
    print("Dine poeng:", score(-1))
    q2()
    
    
def q2():
    q = ["Q1)What is the capital of Norway?" , "Q2)What is the currency of Norway? " , "Q3)What is the largest city in Norway? " , "Q4)When is constitution day (the national day) of Norway? " 
         , "Q5)What color is the background of the Norwegian flag?" , "Q6)How many countries does Norway border? " , "Q7)What is the name of the university in Trondheim? " , "Q8)How long is the border between Norway and Russia? "  
          ,"Q9)Where in Norway is Stavanger? " , "Q10)From which Norwegian city did the world’s famous composer Edvard Grieg come? "]  
    wrong_answ = 0
    
    q2o = ["a.Euro " , "b.Pound" , "c.Krone" , "d.Deutsche Mark "] #lagrer svarene i en liste!


    for i in q2o:
       print("\n"+i)
    a1 = input("Your answer:")
    if a1 in q2o[2]:
     print("Riktig")

     print("Dine poeng:",score(0))
     print(q[2])
     q3()
    else:
       print("Feil!!")
       wrong_answ =wrong_answ+1
       print("Dine poeng:",score(-1))
       print("Feil", wrong_answ)
       print(q[2])
       q3()
       
       
def q3():

    q = ["Q1)What is the capital of Norway?" , "Q2)What is the currency of Norway? " , "Q3)What is the largest city in Norway? " , "Q4)When is constitution day (the national day) of Norway? " 
         , "Q5)What color is the background of the Norwegian flag?" , "Q6)How many countries does Norway border? " , "Q7)What is the name of the university in Trondheim? " , "Q8)How long is the border between Norway and Russia? "  
          ,"Q9)Where in Norway is Stavanger? " , "Q10)From which Norwegian city did the world’s famous composer Edvard Grieg come? "]  
    wrong_answ = 0
   
    q3o = ["a.Oslo" ,"b.Stavanger"  , "c.Bergen" , "d.Trondheim "] 
    

    
    for i in q3o:
       print(i)
    a1 = input("Your answer:")
    if a1 in q3o[0]:
     points = 1
     print("Riktig")
     points = points+1

     print("Dine poeng:",score(1))
     print(q[3])
     q4()
    else:
       print("Feil!!")
       wrong_answ =wrong_answ+1
       points=points-1
       print("Dine poeng:",score(-1))
       print("Feil", wrong_answ)
       print(q[3])
       q4()


def q4():
    q = ["Q1)What is the capital of Norway?" , "Q2)What is the currency of Norway? " , "Q3)What is the largest city in Norway? " , "Q4)When is constitution day (the national day) of Norway? " 
         , "Q5)What color is the background of the Norwegian flag?" , "Q6)How many countries does Norway border? " , "Q7)What is the name of the university in Trondheim? " , "Q8)How long is the border between Norway and Russia? "  
          ,"Q9)Where in Norway is Stavanger? " , "Q10)From which Norwegian city did the world’s famous composer Edvard Grieg come? "]  
    wrong_answ = 0
    q4o = ["a.27th May" ,"b.17th May"  , "c.17th April" , "d.27 April"] 
    

    
    for i in q4o:
     print(i)
    a1 = input("Your answer:")
    if a1 =="b" or a1=="17th May" :
     points = 2   
     print("Riktig")
     print("Dine poeng:",points)
     points = points+1
     print(q[4])
     q5()
    else:
       print("Feil!!")
       wrong_answ =wrong_answ+1
       print("Dine poeng:",points)
       print("Feil", wrong_answ)
       print(q[4])
       q5()

       
def q5():
    q = ["Q1)What is the capital of Norway?" , "Q2)What is the currency of Norway? " , "Q3)What is the largest city in Norway? " , "Q4)When is constitution day (the national day) of Norway? " 
         , "Q5)What color is the background of the Norwegian flag?" , "Q6)How many countries does Norway border? " , "Q7)What is the name of the university in Trondheim? " , "Q8)How long is the border between Norway and Russia? "  
          ,"Q9)Where in Norway is Stavanger? " , "Q10)From which Norwegian city did the world’s famous composer Edvard Grieg come? "]  
    wrong_answ = 0
    points = 4
    q5o = ["a.Red" ,"b.White"  , "c.Blue" , "d.Yellow"] 
    

    
    for i in q5o:
     print(i)
    a1 = input("Your answer:")
    if a1 in q5o[0] :
     print("Riktig")
     points = points+1
     print(q[5])
     q6()
    else:
       print("Feil!!")
       wrong_answ =wrong_answ+1
       print("Dine poeng:",points)
       print("Feil", wrong_answ)
       print(q[5])
       q6() 
 
def q6():
    q = ["Q1)What is the capital of Norway?" , "Q2)What is the currency of Norway? " , "Q3)What is the largest city in Norway? " , "Q4)When is constitution day (the national day) of Norway? " 
         , "Q5)What color is the background of the Norwegian flag?" , "Q6)How many countries does Norway border? " , "Q7)What is the name of the university in Trondheim? " , "Q8)How long is the border between Norway and Russia? "  
          ,"Q9)Where in Norway is Stavanger? " , "Q10)From which Norwegian city did the world’s famous composer Edvard Grieg come? "]  
    wrong_answ = 0
    points = 4
    q6o = ["a.1" ,"b.2"  , "c.3" , "d.4"] 
    

    
    for i in q6o:
     print(i)
    a1 = input("Your answer:")
    if a1 in q6o[2] :
     print("Riktig")
     points = points+1

     print(q[6])
     q7()
    else:
       print("Feil!!")
       wrong_answ =wrong_answ+1
       print("Dine poeng:",points)
       print("Feil", wrong_answ)
       print(q[6])
       q7()
       
def q7():
    q = ["Q1)What is the capital of Norway?" , "Q2)What is the currency of Norway? " , "Q3)What is the largest city in Norway? " , "Q4)When is constitution day (the national day) of Norway? " 
         , "Q5)What color is the background of the Norwegian flag?" , "Q6)How many countries does Norway border? " , "Q7)What is the name of the university in Trondheim? " , "Q8)How long is the border between Norway and Russia? "  
          ,"Q9)Where in Norway is Stavanger? " , "Q10)From which Norwegian city did the world’s famous composer Edvard Grieg come? "]  
    wrong_answ = 0
    points = 5
    q7o = ["a.UiS" ,"b.UiO"  , "c.NMBU" , "d.NTNU"] 
    

    
    for i in q7o:
     print(i)
    a1 = input("Your answer:")
    if a1 in q7o[3] :
     print("Riktig")
     points = points+1

     print("Dine poeng:",points)
    else:
       print("Feil!!")
       wrong_answ =wrong_answ+1
       print("Dine poeng:",points)
       print("Feil", wrong_answ)  
       
def score(p=0):
    po =p
    po=po+1
    print(po)
    if po <0:
     print(po=po-1)
    return po
          
main()    
    