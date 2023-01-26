import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))



rand_letters = random.choices(letters, k=nr_letters)
rand_numbers = random.choices(numbers, k=nr_numbers)
rand_symbols = random.choices(symbols, k=nr_symbols)

total_length = (nr_letters + nr_numbers + nr_symbols)

print(rand_letters)
print(rand_numbers)
print(rand_symbols)
# print(total_length)
merged = [*rand_letters, *rand_numbers, *rand_symbols]
# print(random.shuffle(rand_letters))
# print(random.shuffle(rand_numbers))
# print(random.shuffle(rand_symbols))

pre_pass = ''.join(merged)
print(pre_pass)
# print(type(pre_pass))
password = ''.join(random.sample(pre_pass, k=total_length))
print(f"Your totally random password is: {password}")
