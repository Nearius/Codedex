# 2º Checkpoint - Terminal project, I will try to make a mini-game inspired on POKEMN  I start importing random library and declaring variables for ANSI escape codes (to color the prints)and then a little introduction for the player.

import random
RED = "\033[31m"
GREEN = "\033[32m"
BLUE = "\033[36m"
YELLOW = "\033[33"
BLACK = "\033[30m"
BWHITE = "\033[47m"
RESET = "\033[0m"  # Reset to default color

# We can do the same with text formatting!
ITALICS = "\033[3;30m"
UNDERLINE = "\033[24m"
BOLDRED = "\033[1;31m"
BOLDGREEN = "\033[1;32m"
BOLDWHITE = "\033[1;33m"

print(" _____     ___    _  __   ______   __  __    ___    _   _ ")
print("|  __ \   / _ \  | |/ /  |  ____| |  \/  |  / _ \  | \ | |")
print("| |__) | | | | | |   /   | |___   | \  / | | | | | |  \| |")
print("|  ___/  | | | | |  <    |  ___|  | |\/| | | | | | | . ` |")
print("| |      | |_| | | . \   | |____  | |  | | | |_| | | |\  |")
print("|_|       \___/  |_|\_\  |______| |_|  |_|  \___/  |_| \_| By Nearius")
print("")

print(" _________________________________________________________________________ ")
print(f"|{BWHITE}{BLACK}  Profesor Oak:                                                           {RESET}|")
print(f"|{BWHITE}{BLACK}  Welcome to the world of Pokémon! I'm Professor Oak. Every Pokémon       {RESET}|")
print(f"|{BWHITE}{BLACK}  trainer starts by choosing their very first Pokémon. Today, you get to  {RESET}|")
print(f"|{BWHITE}{BLACK}  to make that choice. Will it be the fiery Charmander, the water-loving  {RESET}|")
print(f"|{BWHITE}{BLACK}  Squirtle, or the plant-powered Bulbasaur? The decision is yours!        {RESET}|")
print(f"|{BWHITE}__________________________________________________________________________{RESET}|")

# I will store each Pokémon with its variable indicating the color it will have, so the code will be cleaner from now on."

Ch = (f"{RED}Charmander{RESET}")
Sq = (f"{BLUE}Squirtle{RESET}")
Bu = (f"{GREEN}Bulbasaur{RESET}")

print(" ________________________________________________________________________")
print(f"|   🔥 {Ch} 🔥   |    💧 {Sq} 💧     |     🌱 {Bu} 🌱     |")   #I know this might bother perfectionists like me, but I have to leave it this way to print correctly in the log.
print("|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|")    
print("| 1. Ember              | 1. Water Gun         | 1. Vine Whip            |")
print("| 2. Scratch            | 2. Tackle            | 2. Growl                |")
print("| 3. Flamethrower       | 3. Bubble            | 3. Leech Seed           |")
print("| 4. Dragon Breath      | 4. Hydro Pump        | 4. Razor Leaf           |")
print("|_______________________|______________________|_________________________|")
print("")

# Now it's time for the player to choose their main Pokémon. I will use a while loop to ensure the player picks a number between 1, 2, or 3. Originally, the main character's rival in Pokémon was 'Gary,' the nephew of Professor Oak. We will also define the Pokémon that your adversary will choose in this game."

mypokemon = 0
garypokemon = 0

while mypokemon != 1 and  mypokemon != 2 and mypokemon != 3:
    mypokemon = int(input(f"Time to choose your starter Pokémon! Type {BOLDWHITE}1{RESET} for {Ch}, {BOLDWHITE}2{RESET} for {Sq}, or {BOLDWHITE}3{RESET} for {Bu}: "))
    if mypokemon != 1 and  mypokemon != 2 and mypokemon != 3:
        print(f"⚠️  Error: You selected '{mypokemon}' but only options 1, 2, or 3 are valid.")
        print(" ")
    else:
        print(" ")

#Now Ill difine the pokemon picked for player and Gary

if mypokemon == 1:
    mypokemon = Ch
    garypokemon = Sq
elif mypokemon == 2:
    mypokemon = Sq
    garypokemon = Bu
else:
    mypokemon = Bu
    garypokemon = Ch  


print(" __________________________________________________________________ ")
print(f"|{BWHITE}{BLACK}  Profesor Oak:                                                   {RESET}|")
print(f"|{BWHITE}{BLACK}  Now that you've made your choice, here's Gary! Remember him?    {RESET}|")
print(f"|{BWHITE}{BLACK}  He's Professor Oak's grandson and your lifelong rival in the    {RESET}|")
print(f"|{BWHITE}{BLACK}  world of Pokémon. He's never one to be outdone, so he's chosen  {RESET}|")
print(f"|{BWHITE}{BLACK}  his own starter Pokémon. Brace yourself; Gary challenges you    {RESET}|")
print(f"|{BWHITE}{BLACK}  to a battle right now to test the mettle of your new Pokémon!   {RESET}|")
print(f"|{BWHITE}__________________________________________________________________{RESET}|")
print(" ")
print(" ")
print("Gary: Ready to learn how real battle Pokemon is done? Let's see if your Pokémon can stand up to mine!")
print (f"{ITALICS}Gary has sent out {garypokemon}!")
print(" ")
print("You: Bring it on, Gary! I believe in my Pokémon, even if we've just started our journey together!")
print(f"{ITALICS}You have sent our {mypokemon}!")