# Simple Function
# def greet():
#     print("Hello Nic")
#     print("What a lovely day!")
#     print("Want something to eat?")
# greet()

# Function that allows for input

# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"What a lovely day {name}")

# greet_with_name("Nic")

#Functions with more than 1 input
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What a lovely day in {location}")

# greet_with("Nic", "Weston") # Positional Argument

# Function with Keyword Argument
greet_with(name="Nic", location="Weston")
