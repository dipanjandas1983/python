
word_list = ["camel", "aardvark", "zebra", "lion", "tiger", "elephant"]

import random

#To Do 1: Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print the chosen word.

chosen_word = random.choice(word_list)

print(f"The chosen word is: {chosen_word}")  # For debugging purposes

# To Do 2: Ask the user to guess a letter and assign it to a variable called guess_letter. Convert the guessed letter to lowercase.

guess_letter = input("Guess a letter: ").lower()

print(f"The guessed letter is: {guess_letter}")  # Fo

# To Do 3: Check if the guessed letter is in the chosen_word. If it is, print a message saying "Correct!" and if not, print "Wrong guess!".

for letter in chosen_word:
    if letter == guess_letter:
        print("Right!")
        break
    else:
        print("Wrong!")
        break
        

   
    

