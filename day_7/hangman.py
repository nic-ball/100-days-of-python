""" Hangman """
import random

word_list = [
    "Adult",
    "Aeroplane",
    "Air",
    "Aircraft",
    "Airforce",
    "Airport",
    "Album",
    "Alphabet",
    "Apple",
    "Arm",
    "Army",
    "Baby",
    "Backpack",
    "Balloon",
    "Banana",
    "Bank",
    "Barbecue",
    "Bathroom",
    "Bathtub",
    "Bed",
    "Bee",
    "Bible",
    "Bird",
    "Bomb",
    "Book",
    "Boss",
    "Bottle",
    "Bowl",
    "Box",
    "Boy",
    "Brain",
    "Bridge",
    "Butterfly",
    "Button",
    "Cappuccino",
    "Car",
    "Carpet",
    "Carrot",
    "Cave",
    "Chair",
    "Chessboard",
    "Chief",
    "Child",
    "Chisel",
    "Chocolates",
    "Church",
    "Circle",
    "Circus",
    "Clock",
    "Clown",
    "Coffee",
    "Coffeeshop",
    "Comet",
    "Compact",
    "Compass",
    "Computer",
    "Crystal",
    "Cup",
    "Cycle",
    "Database",
    "Desk",
    "Diamond",
    "Dress",
    "Drill",
    "Drink",
    "Drum",
    "Dung",
    "Ears",
    "Earth",
    "Egg",
    "Electricity",
    "Elephant",
    "Eraser",
    "Explosive",
    "Eyes",
    "Family",
]
#  Fan, Feather,
#  Festival, Film Finger, Fire, Floodlight, Flower, Foot, Fork, Freeway, Fruit, Fungus, Game,
#  Garden, Gas, Gate, Gemstone, Girl, Gloves, God, Grapes, Guitar, Hammer, Hat, Hieroglyph, Highway,
#  Horoscope, Horse, Hose, Ice, Icecream, Insect, Jet, Junk, Kaleidoscope, Kitchen, Knife,
#  Leather jacket, Leg, Library, Liquid, Magnet, Man, Map, Maze, Meat, Meteor, Microscope,
#  Milk, Milkshake, Mist, Money, Monster, Mosquito, Mouth, Nail, Navy, Necklace, Needle,
#  Onion, Paintbrush, Pants, Parachute, Passport, Pebble, Pendulum, Pepper, Perfume, Pillow,
#  Plane, Planet, Pocket, Post, Potato, Printer, Prison, Pyramid, Radar, Rainbow, Record,
#  Restaurant, Rifle, Ring, Robot, Rock, Rocket, Roof, Room, Rope, Saddle, Salt, Sandpaper,
#  Sandwich, Satellite, School, Sex, Ship, Shoes, Shop, Shower, Signature, Skeleton, Slave,
#  Snail, Software, Solid, Space Shuttle,Spectrum, Sphere, Spice, Spiral, Spoon, Sportscar,
#  Spotlight, Square, Staircase, Star, Stomach, Sun, Sunglasses, Surveyor, Swimming Pool,
#  Sword, Table, Tapestry, Teeth, Telescope, Television, Tennis racquet, Thermometer,
#  Tiger, Toilet, Tongue, Torch, Torpedo, Train, Treadmill, Triangle, Tunnel, Typewriter, Umbrella,
#  Vacuum, Vampire, Videotape, Vulture, Water, Weapon, Web, Wheelchair, Window, Woman, Worm, X-ray"]

chosen_word = random.choice(word_list)
print(chosen_word)
guess = input("Guess a letter: ").lower()

display = []

lives = len(chosen_word - 1)


def guesses():
    for letter in chosen_word:
        if letter == guess:
            display.append(letter)
        else:
            display.append("_")
    return display


while display != chosen_word:
    for char in range(1, chosen_word + 1):
        lives -= 1

print(lives)
