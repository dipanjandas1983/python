## a = 10
## b = 5
###b = 3

###print(a % b)  # Division
##print(a // b)  # Floor division
##print(a ** b)  # Exponentiation
##print(a % b)  # Addition ( remainder of division)

age = int(input("Enter your age: "))

if age <= 18:
    print("You are a minor.")

elif 18 < age < 60:
     print("You are a middle-aged adult.")

elif age >= 60:
        print("You are a senior citizen.")

else:
    print("You are a minor.")