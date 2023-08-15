# Functions with Outputs

f_name = input("What is your first name?: ")
l_name = input("What is your last name?: ")


def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"Welcome {formatted_f_name} {formatted_l_name}!"

formatted_string = format_name(f_name, l_name)
print(formatted_string)
