"""Rock, Paper, Scissors"""
import random

ROCK = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

PAPER = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

SCISSORS = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

game_images = [ROCK, PAPER, SCISSORS]
user_choice = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors \n")
)


if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number! You Lose!")
else:
    print(game_images[user_choice])

    computer_choice = random.randint(0, 2)
    print(f"Computer chose: {computer_choice}")
    print(game_images[computer_choice])

    if user_choice == 0 and computer_choice == 2:
        print("You Win!!")
    elif computer_choice == 0 and user_choice == 2:
        print("You Lose!!")
    elif computer_choice > user_choice:
        print("You Lose!!")
    elif user_choice > computer_choice:
        print("You Win!!")
    elif computer_choice == user_choice:
        print("It's a draw")
