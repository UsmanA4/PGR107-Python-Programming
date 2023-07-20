# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 13:38:46 2023

@author: Usman Ahmad
"""

def main():
    usr =""
    pswd=""
    r_user = ["PGR107"]
    r_pass = ["Python"]
    password_store = {}
    q = ["Q1)What is the capital of Norway?", "Q2)What is the currency of Norway? ", "Q3)What is the largest city in Norway? ", "Q4)When is constitution day (the national day) of Norway? ", "Q5)What color is the background of the Norwegian flag?", "Q6)How many countries does Norway border? ",
         "Q7)What is the name of the university in Trondheim? ", "Q8)How long is the border between Norway and Russia? ", "Q9)Where in Norway is Stavanger? ", "Q10)From which Norwegian city did the world’s famous composer Edvard Grieg come? "]    
    while (usr != "PGR107" and r_pass != "Python"):

        usr = input("Enter username:")
        pswd = input("Enter password:")
        password_store[usr] = pswd 
        if(usr == r_user[0] and pswd == r_pass[0]):
            print(q[0])
            runQuiz()
        else:
             print("Invalid username and/or password")

def runQuiz():
    solution_store = {}
    questions_store={}
    points =0
    wrong = 0
    q = ["Q1)What is the capital of Norway?", "Q2)What is the currency of Norway? ", "Q3)What is the largest city in Norway? ", "Q4)When is constitution day (the national day) of Norway? ", "Q5)What color is the background of the Norwegian flag?", "Q6)How many countries does Norway border? ",
         "Q7)What is the name of the university in Trondheim? ", "Q8)How long is the border between Norway and Russia? ", "Q9)Where in Norway is Stavanger? ", "Q10)From which Norwegian city did the world’s famous composer Edvard Grieg come? "]    
    
    
    q1o = ["a. Bergen", "b. Oslo", "c. Stavanger", "d. Trondheim"]

    for i in q1o:
        print(i)
    a1 = input("Your answer:")
    if a1 in q1o[1]:
        points = points+1
        print("Riktig")
        print("Your points:",points )
        print(q[1])
        
    else :
        wrong=wrong+1
        print("Feil!!")
        print("Fei:",wrong)
        print("Your points:", points)     
        solution_store[q1o[1]] = a1
        questions_store[q[1]] =a1
        print(q[1])
    
    q2o = ["a.Euro ", "b.Pound", "c.Krone", "d.Deutsche Mark "]   
    
    for i in q2o:
        print(i)
    a1 = input("Your answer:")
    if a1 in q2o[2]:
        points = points+1
        print("Riktig")
        print("Your points:",points )
        print(q[2])
        
    else :
        wrong=wrong+1
        print("Feil!!")
        print("Fei:",wrong)
        print("Your points:", points)     
        solution_store[q2o[2]] = a1
        questions_store[q[1]] =a1
        
        print(q[2])
        
    q3o = ["a.Oslo ", "b.Stavanger", "c.Bergen", "d.Trondheim "]    
    
    for i in q3o:
        print(i)
    a1 = input("Your answer:")
    if a1 in q3o[0]:
        points = points+1
        print("Riktig")
        print("Your points:",points )
        print(q[3])
        
    else :
        wrong=wrong+1
        print("Feil!!")
        print("Fei:",wrong)
        print("Your points:", points)     
        solution_store[q3o[0]] = a1
        questions_store[q[2]] =a1
        print(q[3])
        
    q4o = ["a.27th May", "b.17th May", "c.17th April", "d.27 April"]
    
    for i in q4o:
        print(i)
    a1 = input("Your answer:")
    if a1 in q4o[1]:
        points = points+1
        print("Riktig")
        print("Your points:",points )
        print(q[4])
        
    else :
        wrong=wrong+1
        print("Feil!!")
        print("Fei:",wrong)
        print("Your points:", points)     
        solution_store[q4o[1]] = a1
        questions_store[q[3]] =a1
        print(q[4])
        
    q5o = ["a.Red", "b.White", "c.Blue", "d.Yellow"]

    for i in q5o:
         print(i)
    a1 = input("Your answer:")
    if a1 in q5o[0]:
        print("Riktig")
        points=points+1
        print("Your points:",points)
        print(q[5])
        
    else :
        wrong=wrong+1
        print("Feil!!")
        print("Fei:",wrong)
        print("Your points:", points)     
        solution_store[q5o[0]] = a1
        questions_store[q[4]]=a1
        print(q[5])
        
        
    q6o = ["a.1", "b.2", "c.3", "d.4"]
    
    for i in q6o:
         print(i)
    a1 = input("Your answer:")
    if a1 in q6o[2]:
        print("Riktig")
        points=points+1
        print("Your points:",points)
        print(q[6])
        
    else :
        wrong=wrong+1
        print("Feil!!")
        print("Fei:",wrong)
        print("Your points:", points)     
        solution_store[q6o[2]] = a1
        questions_store[q[5]] =a1
        print(q[6])
        
        
    q7o = ["a.UiS", "b.UiO", "c.NMBU", "d.NTNU"]
    
    for i in q7o:
          print(i)
    a1 = input("Your answer:")
    if a1 in q7o[3]: 
         print("Riktig")
         points=points+1
         print("Your points:",points)
         print(q[7])
         
    else :
        wrong=wrong+1
        print("Feil!!")
        print("Fei:",wrong)
        print("Your points:", points)     
        solution_store[q7o[3]] = a1
        questions_store[q[6]] =a1
        print(q[7])
        
    q8o = ["a.96 km", "b.196 km", "c.296 km", "d.396 km"]
    
    for i in q8o:
        print(i)
    a1 = input("Your answer:")
    if a1 in q8o[1]:
        print("Riktig")
        points=points+1
        print("Your points:",points)
        print(q[8])
        
    else :
        wrong=wrong+1
        print("Feil!!")
        print("Fei:",wrong)
        print("Your points:", points)     
        solution_store[q8o[1]] = a1
        questions_store[q[7]] =a1
        print(q[8])
        
    q9o = ["a.North", "b.South", "c.South-west", "d.South-east"]
    
    for i in q9o:
      print(i)
    a1 = input("Your answer:")
    if a1 in q9o[2]:
        print("Riktig")
        points=points+1
        print("Your points:",points)
        print(q[9])
        
    else :
        wrong=wrong+1
        print("Feil!!")
        print("Fei:",wrong)
        print("Your points:", points)     
        solution_store[q9o[2]] = a1
        questions_store[q[8]] =a1
        print(q[9])
        
    q10o = ["a.Oslo", "b.Bergen", "c.Stavanger", "d.Tromsø"] 
    
    for i in q10o:
       print(i)
    a1 = input("Your answer:")
    if a1 in q10o[1]:
         print("Riktig")
         points=points+1
         print("Your points:",points)   
         
    else :
        wrong=wrong+1
        print("Feil!!")
        print("Fei:",wrong)
        print("Your points:", points)     
        solution_store[q10o[1]] = a1
        questions_store[q[9]] =a1
        
        
        
    print("Antall riktige" , points)
    
    
    print("Antall feil", wrong)    
    
    
    print("Questions answered wrong:", questions_store)
    
    print("Ditt svar og Fasit svar på spørsmålene du svarte feil på", solution_store)

    
    
    
main()