# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 09:25:35 2023

@author: ....
"""

import random

# Function to read words from the file and return a random word
def read_words():
    filename = 'C:/Users/peiwa/OneDrive/Skrivebord/words.txt'  # Replace this with the name of your text file

    # Open the file and read its content
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Split the content into words 
    words = content.split()
    # Pick a random word and remove any surrounding whitespace
    random_word = random.choice(words).strip()
    return random_word




# Function to print the guessed word with underscores for unguessed characters
def print_guessed_word(guessed_word):
    for char in guessed_word:
        print(char, end="")
        
    

# Main function for the guessing game
def guessing_game():
    # Get a random word
    word = read_words()
    word_length = len(word)
    # Create an initial guessed word with underscores
    guessed_word = ['_' for _ in range(word_length)]
    remaining_guesses = word_length

    # Print initial game information
    print("The word you need to guess has ", word_length, " characters.")
    print("You have now " , remaining_guesses , " guesses")
    
    # Continue the game while there are remaining guesses and unguessed characters
    while remaining_guesses > 0 and '_' in guessed_word:
        print_guessed_word(guessed_word)
        guess = input("Guess a character: ").lower()

        # Check if the guessed letter is already in the guessed word
        if guess in guessed_word:
            print("You have already guessed the letter " +  guess )
        # Check if the input is a single letter
        elif len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter (A-Z).")
        else:
            found = False
            # Check if the guessed letter is in the word
            for i, char in enumerate(word):
                if char == guess:
                    guessed_word[i] = guess
                    found = True

            # Update the guessed word based on the guessed letter
            if found:
                print_guessed_word(guessed_word)
            else:
                remaining_guesses -= 1
                print("Sorry, the letter " + guess +" is not in the word.")
                print_guessed_word(guessed_word)

            # Print the remaining guesses
            print("You have ",  remaining_guesses , "guess(es) left.")
            print("-" * 40)

    # Check if the word is fully guessed or if the guesses ran out
    if '_' not in guessed_word:
        print("Congratulations! You have guessed the word " + word + " correctly.")
    else:
        print("Sorry, you have run out of guesses. The word was " + word)

# Start the guessing game
guessing_game()
