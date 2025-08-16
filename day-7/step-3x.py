
import random

word_list = ["camel", "aardvark", "zebra", "lion", "tiger", "elephant"]

chosen_word = random.choice(word_list)
print(chosen_word)


#To Do 4: create a display that put the guessed letter in the right position and "_" in remaining places

game_over = False
correct_word = []

while not game_over:

    guess = input(f"Guess the letter : ").lower()
    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_word.append(letter)

        elif letter in correct_word:
            display += letter
        
        else:
            display += "_"


    print(display)

    if "_" not in display:

        game_over = True

        print("you win")


















        



