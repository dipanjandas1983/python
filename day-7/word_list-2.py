word_list = ["camel", "aardvark", "zebra", "lion", "tiger", "elephant"]

import random

guess_letter = input("Guess a letter: ").lower()

guess = random.choice(guess_letter)

print(f"The guessed letter is: {guess}")  # For debugging purposes