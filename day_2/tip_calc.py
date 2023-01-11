print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? \n"))

tip = int(input("What percentage tip would you like to leave? 10, 12 or 15 \n"))
final_tip = (tip / 100) + 1
split_between = int(input("How many people is the bill to be split between? \n"))

total = (bill / split_between) * final_tip
print(f"Each person should pay: £{total:.2f}")
