#To Do 1: chooose a word from the word list and assigne it to a variable called chosen_word


import random

word_list = ["camel", "aardvark", "zebra", "lion", "tiger", "elephant"]

chosen_word = random.choice(word_list)

print(chosen_word)


#To Do 2: Ask the user to guess a letter and assign it to a variable called guess

guess = input(f"Guess a letter: ").lower()

print(guess)



#To Do 3: check if the guessed letter is in the chosen word then print "Right!" or "Wrong!"

for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")

    

    





