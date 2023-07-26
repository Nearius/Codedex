# 2º Checkpoint - Terminal project, I will try to make a mini-game inspired on POKEMN  I start importing random library and then a little introduction for the player.

import random

print(" _____     ___    _  __   ______   __  __    ___    _   _ ")
print("|  __ \   / _ \  | |/ /  |  ____| |  \/  |  / _ \  | \ | |")
print("| |__) | | | | | |   /   | |___   | \  / | | | | | |  \| |")
print("|  ___/  | | | | |  <    |  ___|  | |\/| | | | | | | . ` |")
print("| |      | |_| | | . \   | |____  | |  | | | |_| | | |\  |")
print("|_|       \___/  |_|\_\  |______| |_|  |_|  \___/  |_| \_| By Nearius")
print("")

print(" _________________________________________________________________________ ")
print("|                                                                          |")
print("|  Welcome to the world of Pokémon! I'm Professor Oak. Every Pokémon       |")
print("|  trainer starts by choosing their very first Pokémon. Today, you get to  |")
print("|  to make that choice. Will it be the fiery Charmander, the water-loving  |")
print("|  Squirtle, or the plant-powered Bulbasaur? The decision is yours!        |")
print("|__________________________________________________________________________|")

print(" ________________________________________________________________________")
print("|   🔥 Charmander 🔥   |    💧 Squirtle 💧     |     🌱 Bulbasaur 🌱     |")   #I know this might bother perfectionists like me, but I have to leave it this way to print correctly in the log.
print("|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|")    
print("| 1. Ember              | 1. Water Gun         | 1. Vine Whip            |")
print("| 2. Scratch            | 2. Tackle            | 2. Growl                |")
print("| 3. Flamethrower       | 3. Bubble            | 3. Leech Seed           |")
print("| 4. Dragon Breath      | 4. Hydro Pump        | 4. Razor Leaf           |")
print("|_______________________|______________________|_________________________|")
print("")

#Now it's time to choose main pokemon of the player, I will use a while loop to warranty the player choose a number between 1, 2 or 3
mypokemon = 0

while mypokemon != 1 and 2 and 3:
    mypokemon = int(input("Type 1) to choose Charmander, 2) to choose Squirtle, or 3) to choose Bulbasaur: "))
    print(f"⚠️  You selected '{mypokemon}' but only options 1, 2, or 3 are available.")
print("final del loop", mypokemon)