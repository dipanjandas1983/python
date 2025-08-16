print("Welcome to the Treasure Island Adventure")

side = input("You are at a crossroad. Do you want to go left or right? ").lower()
if side == "left":
    action = input("You come to a lake. Do you want to swim or wait for a boat? ").lower()
    if action == "wait":
        print("You wait for a boat and cross the lake safely. You find a treasure chest!")
        door = input("You arrive at a house with three doors: red, yellow, and blue. Which door do you choose? ").lower()
        if door == "red":
            print("You enter a room full of fire. Game over.")
        elif door == "blue":
            print("You enter a room with beasts. Game over.")
        elif door == "yellow":
            print("You found the treasure! You win!")
        else:
            print("That's not a valid door. Game over.")
    elif action == "swim":
        print("You try to swim across the lake but are eaten by a crocodile. Game over.")
    else:
        print("Invalid choice at the lake. Game over.")
else:
    print("You fell into a hole. Game over.")
