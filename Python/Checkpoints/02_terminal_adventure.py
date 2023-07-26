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
print("|_|       \___/  |_|\_\  |______| |_|  |_|  \___/  |_| \_|")
print("")

print(" _________________________________________________________________________ ")
print(f"|{BWHITE}{BLACK}  Profesor Oak:                                                           {RESET}|")
print(f"|{BWHITE}{BLACK}  Welcome to the world of Pokémon! I'm Professor Oak. Every Pokémon       {RESET}|")
print(f"|{BWHITE}{BLACK}  trainer starts by choosing their very first Pokémon. Today, you get to  {RESET}|")
print(f"|{BWHITE}{BLACK}  to make that choice. Will it be the fiery Charmander, the water-loving  {RESET}|")
print(f"|{BWHITE}{BLACK}  Squirtle, or the plant-powered Bulbasaur? The decision is yours!        {RESET}|")
print(f"|{BWHITE}__________________________________________________________________________{RESET}|")
print(" ")


# I will store each Pokémon with its variable indicating the color it will have, so the code will be cleaner from now on.and also his attacks, hp, and lvl's"

Ch = (f"{RED}Charmander{RESET}")
Ch_LvL = 5 ; Ch_HP = 28
Ch_attack1_name= "Ember" ; Ch_attack1_damage = 6
Ch_attack2_name= "Scratch" ; Ch_attack2_damage = 5
Ch_attack3_name= "Flamethrower" ; Ch_attack3_damage = 8
Ch_attack4_name= "Dragon Breath" ; Ch_attack4_damage = 7

Sq = (f"{BLUE} Squirtle {RESET}")
Sq_LvL = 5 ; Sq_HP = 30
Sq_attack1_name= "Water Gun" ; Sq_attack1_damage = 6
Sq_attack2_name= "Tackle" ; Sq_attack2_damage = 5
Sq_attack3_name= "Bubble" ; Sq_attack3_damage = 6
Sq_attack4_name= "Hydro Pump" ; Sq_attack4_damage = 8

Bu = (f"{GREEN}Bulbasaur {RESET}")
Bu_LvL = 5 ; Bu_HP = 29
Bu_attack1_name= "Vine Whip" ; Bu_attack1_damage = 6
Bu_attack2_name= "Headbutt" ; Bu_attack2_damage = 5
Bu_attack3_name= "Leech Seed" ; Bu_attack3_damage = 6
Bu_attack4_name= "Razor Leaf" ; Bu_attack4_damage = 7

print(" ________________________________________________________________________")
print(f"|   🔥 {Ch} 🔥   |   💧 {Sq} 💧    |     🌱 {Bu}🌱     |")   #I know this might bother perfectionists like me, but I have to leave it this way to print correctly in the log.
print("|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|")    
print(f"| 1. {Ch_attack1_name}              | 1. {Sq_attack1_name}         | 1. {Bu_attack1_name}            |")
print(f"| 2. {Ch_attack2_name}            | 2. {Sq_attack2_name}            | 2. {Bu_attack2_name}             |")
print(f"| 3. {Ch_attack3_name}       | 3. {Sq_attack3_name}            | 3. {Bu_attack3_name}           |")
print(f"| 4. {Ch_attack4_name}      | 4. {Sq_attack4_name}        | 4. {Bu_attack4_name}           |")
print("|_______________________|______________________|_________________________|")
print("")
print("")

# Now it's time for the player to choose their main Pokémon. First I create the variable for the pokemon and his atributes for each trainer, then I will use a "while" loop to ensure the player picks a number between 1, 2, or 3. Originally, the main character's rival in Pokémon was 'Gary,' the grandson of Professor Oak. We will also define the Pokémon that your adversary will choose in this game."

MyPokemon = 0
My_LvL = 0 ; My_HP = 1 ; My_xp = 0
My_attack1_name= " " ; My_attack1_damage = 0
My_attack2_name= " " ; My_attack2_damage = 0
My_attack3_name= " " ; My_attack3_damage = 0
My_attack4_name= " " ; My_attack4_damage = 0

GaryPokemon = 0
Ga_LvL = 0 ; My_HP = 1 ; Ga_xp = 0
Ga_attack1_name= " " ; Ga_attack1_damage = 0
Ga_attack2_name= " " ; Ga_attack2_damage = 0
Ga_attack3_name= " " ; Ga_attack3_damage = 0
Ga_attack4_name= " " ; Ga_attack4_damage = 0

while MyPokemon != 1 and  MyPokemon != 2 and MyPokemon != 3:
    MyPokemon = int(input(f"Time to choose your starter Pokémon! Type {BOLDWHITE}1{RESET} for {Ch} {BOLDWHITE}2{RESET} for {Sq} or {BOLDWHITE}3{RESET} for {Bu}: "))
    if MyPokemon != 1 and  MyPokemon != 2 and MyPokemon != 3:
        print(f"⚠️  Error: You selected '{MyPokemon}' but only options 1, 2, or 3 are valid.")
        print(" ")
    else:
        print(" ")

#Now Ill difine the pokemon picked for player and Gary and his respective atributes

if MyPokemon == 1:
    MyPokemon = Ch
    My_LvL = Ch_LvL ; My_HP = Ch_HP ;  My_xp = 0
    My_attack1_name= Ch_attack1_name ; My_attack1_damage = Ch_attack1_damage
    My_attack2_name= Ch_attack2_name ; My_attack2_damage = Ch_attack2_damage
    My_attack3_name= Ch_attack3_name ; My_attack3_damage = Ch_attack3_damage
    My_attack4_name= Ch_attack4_name ; My_attack4_damage = Ch_attack4_damage

    GaryPokemon = Sq
    Ga_LvL = Sq_LvL ; Ga_HP = Sq_HP ;  Ga_xp = 0
    Ga_attack1_name= Sq_attack1_name ; Ga_attack1_damage = Sq_attack1_damage
    Ga_attack2_name= Sq_attack2_name ; Ga_attack2_damage = Sq_attack2_damage
    Ga_attack3_name= Sq_attack3_name ; Ga_attack3_damage = Sq_attack3_damage
    Ga_attack4_name= Sq_attack4_name ; Ga_attack4_damage = Sq_attack4_damage

elif MyPokemon == 2:
    MyPokemon = Sq
    My_LvL = Sq_LvL ; My_HP = Sq_HP ;  My_xp = 0
    My_attack1_name= Sq_attack1_name ; My_attack1_damage = Sq_attack1_damage
    My_attack2_name= Sq_attack2_name ; My_attack2_damage = Sq_attack2_damage
    My_attack3_name= Sq_attack3_name ; My_attack3_damage = Sq_attack3_damage
    My_attack4_name= Sq_attack4_name ; My_attack4_damage = Sq_attack4_damage

    GaryPokemon = Bu
    Ga_LvL = Bu_LvL ; Ga_HP = Bu_HP ;  Ga_xp = 0
    Ga_attack1_name= Bu_attack1_name ; Ga_attack1_damage = Bu_attack1_damage
    Ga_attack2_name= Bu_attack2_name ; Ga_attack2_damage = Bu_attack2_damage
    Ga_attack3_name= Bu_attack3_name ; Ga_attack3_damage = Bu_attack3_damage
    Ga_attack4_name= Bu_attack4_name ; Ga_attack4_damage = Bu_attack4_damage

else:
    MyPokemon = Bu
    My_LvL = Bu_LvL ; My_HP = Bu_HP ;  My_xp = 0
    My_attack1_name= Bu_attack1_name ; My_attack1_damage = Bu_attack1_damage
    My_attack2_name= Bu_attack2_name ; My_attack2_damage = Bu_attack2_damage
    My_attack3_name= Bu_attack3_name ; My_attack3_damage = Bu_attack3_damage
    My_attack4_name= Bu_attack4_name ; My_attack4_damage = Bu_attack4_damage

    GaryPokemon = Ch
    Ga_LvL = Ch_LvL ; Ga_HP = Ch_HP ;  Ga_xp = 0
    Ga_attack1_name= Ch_attack1_name ; Ga_attack1_damage = Ch_attack1_damage
    Ga_attack2_name= Ch_attack2_name ; Ga_attack2_damage = Ch_attack2_damage
    Ga_attack3_name= Ch_attack3_name ; Ga_attack3_damage = Ch_attack3_damage
    Ga_attack4_name= Ch_attack4_name ; Ga_attack4_damage = Ch_attack4_damage


print(MyPokemon)
print(My_LvL, My_HP, My_xp) 
print(My_attack1_name, My_attack1_damage) 
print(My_attack2_name, My_attack2_damage)
print(My_attack3_name, My_attack3_damage )
print(My_attack4_name, My_attack4_damage) 

print(" ")
print(GaryPokemon)
print(Ga_LvL, Ga_HP, Ga_xp) 
print(Ga_attack1_name, Ga_attack1_damage) 
print(Ga_attack2_name, Ga_attack2_damage)
print(Ga_attack3_name, Ga_attack3_damage )
print(Ga_attack4_name, Ga_attack4_damage) 


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
print("Gary: Ready to learn how real Pokemon battle is done? Let's see if your Pokémon can stand up to mine!")
print (f"Come on, {GaryPokemon}! {ITALICS}Gary has sent out {GaryPokemon}")
print(" ")
print("You: Bring it on, Gary! I believe in my Pokémon, even if we've just started our journey together!")
print(f"Come on, {MyPokemon}! {ITALICS}You have sent out {MyPokemon}")


#Combat variables that I need to procees the combat, 

Action = 0
Turn = 0


while My_HP != 20 and Ga_HP != 20:
    print(" __________________________________________________________ ")
    print("|                                                          |")
    print(f"| {GaryPokemon}    Lv {Ga_LvL}                                       |")
    print(f"| Hp:{Ga_HP}                                                    |")
    print(f"|                                       {MyPokemon}    Lv {My_LvL} |")
    print(f"|                                                    Hp:{My_HP} |")
    print("|__________________________________________________________| ")
    print(f"|What will {MyPokemon} do?                                  | ")
    print(f"|     {BOLDWHITE}1{RESET} Fight    {BOLDWHITE}2{RESET} Pokemon       {BOLDWHITE}3{RESET} Bag         {BOLDWHITE}4{RESET} Run       | ")
    print(f"|__________________________________________________________| ")

    while Action != 1 and Action != 2 and Action != 3 and Action != 4:
          Action = int(input("Type your option here: "))
          if Action == 1:
            int(input("Choose attack: {BOLDWHITE}→ 1{RESET} {My_attack1_name} - {BOLDWHITE}→ 2{RESET} {My_attack2_name} - {BOLDWHITE}→ 3{RESET} {My_attack3_name} - {BOLDWHITE}→ 4{RESET} {My_attack4_name} "))
                  
  
    print("fin bucle")