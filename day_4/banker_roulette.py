import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

# num_items = len(names)
# random_choice = random.randint(0, num_items - 1)

person_who_will_pay = random.choice(names)
print(person_who_will_pay + " is going to pay today.")
