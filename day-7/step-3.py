
import random

word_list = ["camel", "aardvark", "zebra", "lion", "tiger", "elephant"]



#To Do 1: Create a placeholder with same number of the blanks as the chosen_word 
# if the chosen_word is "apple" then the placeholder will be with "_ _ _ _ _"

chosen_word = random.choice(word_list)
placeholder = "_"

print(chosen_word)

word_len = len(chosen_word)

for i in range(word_len):

    placeholder += "_"

#To Do 2: if the guess letter is right from the chosen_word then put it in right position and placeholder _ for rest 
#To Do 3: Keep on guessing till the word is comming with righ letters

game_over = False

correct_letter = []

while not game_over:

    guess = input(f"Guess the letter : ").lower()

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

        print(f"You win")









