print(f"welcome to the calculator")
bill = float(input("Enter the bill amount: "))
tip = float(input("Enter the tip percentage of the tip would you like to give 10 15 20: "))
people = int(input("Enter the number of people: "))
total_bill_plus_tip = tip / 100 * bill + bill
perperson_share = total_bill_plus_tip / people

print(total_bill_plus_tip)
print(f"Each person should pay: {perperson_share:.2f}")

