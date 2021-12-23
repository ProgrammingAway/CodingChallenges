print("Welcome to the Tip Calculator!")
total = float(input("What was the bill total? $"))
people = int(input("How many people to split the bill? "))
tip = int(input("What percentage tip would you like to give? "))
tipMultiple = (tip/100) + 1
personTotal = total * tipMultiple / people
answer = round(personTotal, 2)

print("Each person should pay: $" + str(answer))
print(f"Each person should pay: ${answer}")