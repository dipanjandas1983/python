number_of_hurdles = 3  # Set the number of hurdles to clear this many time you have to jump input 

while number_of_hurdles > 0:
    jump_height = int(input("Enter your jump height: "))
    
    if jump_height >= 5:
        print("You cleared the hurdle!")
        number_of_hurdles -= 1
    else:
        print("You failed to clear the hurdle. Try again!")

# This runs after the while loop is done
print("🎉 Congratulations! You cleared all the hurdles!")
