height = int(input("Enter your height in cm: "))
bill = 0

if height >= 150:
    print("You are tall enough to ride the roller coaster!")
    
    age = int(input("Enter your age: "))
    if age <= 12:
        print("Please pay INR 10 for the ride.")
        bill = 10
    elif age <= 18:
        print("Please pay INR 30 for the ride.")
        bill = 30
    elif age <= 30:
        print("Please pay INR 40 for the ride.")
        bill = 40
    else:
        print("Please pay INR 60 for the ride.")
        bill = 60
        
    if age >= 40 and age <= 55:
        print("No worries, you can ride for free!")
        bill = 60
        
    if age > 55:
        print("You get a senior citizen discount of 10%!")
        bill = 60 * 0.9
        
    photo = input("Do you want a photo taken? (yes/no): ")
    
    if photo.lower() == "yes": 
        bill += 15
        
    print(f"Your total bill is INR {bill}.")
else:
    print("Sorry, you are not tall enough to ride the roller coaster.")