import random

friends = ["Alice", "Bob", "Charlie", "David", "Emuel"]


# option 1: Randomly select a friend to pay the bill
print(random.choice(friends))

# option 2: Randomly select a friend using an index

random_index = random.randint(0, 4)

print(friends[random_index])