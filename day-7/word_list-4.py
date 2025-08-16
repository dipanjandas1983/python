
word_list = ["camel", "aardvark", "zebra", "lion", "tiger", "elephant"]

import random

stages = [
    # 0 = Full hangman
    """
     ------
     |    |
     |    O
     |   /|\\
     |   / \\
     |
    _|_
    """,
    # 1
    """
     ------
     |    |
     |    O
     |   /|\\
     |   / 
     |
    _|_
    """,
    # 2
    """
     ------
     |    |
     |    O
     |   /|\\
     |   
     |
    _|_
    """,
    # 3
    """
     ------
     |    |
     |    O
     |   /|
     |   
     |
    _|_
    """,
    # 4
    """
     ------
     |    |
     |    O
     |    |
     |   
     |
    _|_
    """,
    # 5
    """
     ------
     |    |
     |    O
     |   
     |   
     |
    _|_
    """,
    # 6 = Starting stage (empty gallows)
    """
     ------
     |    |
     |    
     |   
     |   
     |
    _|_
    """
]



#To Do 1: Create a "placeholder" with the same number of underscores as the number of letters in the word

chosen_word = random.choice(word_list)

word_length = len(chosen_word)

print(chosen_word)

placeholder = "_"

for letter in range(0, 5):
    placeholder += "_"


print(placeholder)

##To Do 2: Create a "placeholder" with the same number of underscores as the number of character in the word

for letter in range(word_length):
    placeholder += "_"

print(word_length)
   
    

## To Do 3: Create a display that puts the guessed letters in the right positions and underscores for the rest

game_over = False

correct_letter = []

while not game_over:

    guess = input("Guess a letter:").lower()

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letter.append(letter)
            
        elif letter in correct_letter:
            display += letter

        else:
            display += "_"
    print(display)

    if "_" not in display:
        game_over = True
        
        print("You win!")

    else:
        print("you loose!")
        break

