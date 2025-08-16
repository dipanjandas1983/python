
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

import random 

chosen_word = random.choice(word_list)

print(chosen_word)

# To Do 1: Print the ASCII 
# if you choose the correct letter then hang man will remain in stage 6 , 
# for each wrong word chosen the hang man will form 
# and it will go till the stage 1 with full hang man structure 
# that's how we can decide how many lives left for the players 



lives = 6
correct_word = []
game_over = False 

while not game_over:
    guess = input(f"Guess the letter : ").lower()
    display = ""


    for letter in chosen_word:
        if guess == letter:
            display += letter
            correct_word.append(guess)

        elif letter in correct_word:
            display += letter

        else: 
            display += "_"

    print(display)

    if guess not in chosen_word:
        lives -= 1
        print("You lost a life")
               
        print(stages[lives])
        print(f"lives left : ", lives)

    if "_" not in display:
        game_over = True
        print("you win")
        print("with available lives : ", lives)

      
    elif lives == 0:
       game_over = True
       print("You loose")


if lives >= 1 and lives <=2:
        print("You Passed , Poor performance")
elif lives >= 2 and lives <=4:
        print("Good Performance")
elif lives >=4 and lives == 6:
        print("Excellent Performance")

    
        

    
    
            
        
  

    
        
  

       



