print("Welcome to the tip calculator!")
bill = input("What was the total bill? \n")

bill_as_float = float(bill)
tip = input("What percentage tip would you like to leave? 10, 12 or 15 \n")
final_tip = (float(tip) / 100) + 1
split_between = input("How many people is the bill to be split between? \n")
split_float = float(split_between)
total = (bill_as_float / split_float) * final_tip
print(f"Each person should pay: £{total:.2f}")
