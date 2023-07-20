# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 08:58:28 2023

@author: Usman Ahmad
"""



class Movies:
    
   def __init__(self , title , releaseYear, genre):
       self.title = title
       self.releaseYear = releaseYear
       self.genre = genre
       
   
   def checkGenre(movie):
        genre = "Action"
        
        if(genre ==movie.genre):
            print("\n"+genre, ":")
            print(movie.title , str(movie.releaseYear) , movie.genre)
        else:
            print("\nSorry , this movie does not fulfill the requirements:")
            print(movie.title , str(movie.releaseYear) , movie.genre)
   def checkReleaseYear(mov):
        year = 2019
        if(mov.releaseYear>=year):
         print("\nResults found for the searched year:")   
         print(mov.title , str(mov.releaseYear) , mov.genre) 

                 

m1 = Movies("La la land", 2019, "Drama")        
m2 = Movies("Avengers", 2012, "Action")   
m3 = Movies("Knives Out", 2020, "Thriller") 
m4 = Movies("21 Bridges",2017,"Thriller")
m5 = Movies("Kingsman",2011,"Action")

m1.checkGenre()
m2.checkGenre()
m3.checkGenre()
m4.checkGenre()
m5.checkGenre()
m1.checkReleaseYear()
m2.checkReleaseYear()
m3.checkReleaseYear()
m4.checkReleaseYear()
m5.checkReleaseYear()