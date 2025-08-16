import random

word_list = ["camel", "aardvark", "zebra", "lion", "tiger", "elephant"]

#To Do 3 : Create a placeholder with same number of the blanks as the chosen_word with "_


chosen_word = random.choice(word_list)
print(chosen_word)
word_len = len(chosen_word)
display = []


guess = input(f"Guess the letter : ")

placeholder = ""

for letter in range(word_len):
    placeholder += "_"

print(placeholder)







