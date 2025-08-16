import random

word_list = ["camel", "aardvark", "zebra", "lion", "tiger", "elephant"]


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

#To Do 1: Create a placeholder with same number of the blanks as the chosen_word 
# if the chosen_word is "apple" then the placeholder will be with "_ _ _ _ _"
chosen_word = random.choice(word_list)
placeholder = "_"

print(chosen_word)

word_len = len(chosen_word)

for i in range(word_len):

    placeholder += "_"

#print(placeholder)

#To Do 2: check if the guess letter is right from the chosen_word then put it in right position and placeholder _ for rest 

guess = input(f"Guess the letter : ").lower()

display = ""

for letter in chosen_word:
    if letter == guess:
        display += letter
    else:
        display += "_"

print(display)

        





