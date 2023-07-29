#<Terminal project, My 2n CheckPoint> I will try to make a mini-game inspired on POKEMoN  I start importing "random" library and declaring variables for ANSI escape codes (to color the prints).

import random

RED = "\033[31m"
GREEN = "\033[32m"
BLUE = "\033[36m"
BLACK = "\033[30m"
BWHITE = "\033[47m"
RESET = "\033[0m"  # Reset to default color

# We do the same with text formatting!
ITALICS = "\033[3;30m"
UNDERLINE = "\033[24m"
BOLDRED = "\033[1;31m"
BOLDGREEN = "\033[1;32m"
BOLDWHITE = "\033[1;33m"
BOLDBLACK = "\033[1;30m"
BOLDBLUE = "\033[1;36m"

# Introduction, We ask for the player's name for subsequent texts.
print(" _____     ___    _  __   ______   __  __    ___    _   _ ")
print("|  __ \   / _ \  | |/ /  |  ____| |  \/  |  / _ \  | \ | |")
print("| |__) | | | | | |   /   | |___   | \  / | | | | | |  \| |")
print("|  ___/  | | | | |  <    |  ___|  | |\/| | | | | | | . ` |")
print("| |      | |_| | | . \   | |____  | |  | | | |_| | | |\  |")
print("|_|       \___/  |_|\_\  |______| |_|  |_|  \___/  |_| \_|  By Nearius" )
print("")

print(" _________________________________________________________________________ ")
print(f"|{BWHITE}{BLACK}  🧓 Profesor Oak 🧓                                                      {RESET}|")
print(f"|{BWHITE}{BLACK}  Welcome to the world of Pokémon! I'm Professor Oak. Every Pokémon       {RESET}|")
print(f"|{BWHITE}{BLACK}  trainer starts by choosing their very first Pokémon. Today, you get to  {RESET}|")
print(f"|{BWHITE}{BLACK}  to make that choice. Will it be the fiery Charmander, the water-loving  {RESET}|")
print(f"|{BWHITE}{BLACK}  Squirtle, or the plant-powered Bulbasaur? The decision is yours!        {RESET}|")
print(f"|{BWHITE}__________________________________________________________________________{RESET}|")
print(" ")
PlayerName = input(f"🧓 Oak: Before you begin your journey, please tell me, what is your name?: ")
print(f"🧓 Oak: Oh yes, {PlayerName}! Now I remember you!")
print("🧓 Oak: Now it's time to choose your first Pokemon 😃")
input(f"{ITALICS}>> Press [ENTER] to continue <<{RESET}")
print(" ")
print(f"🧓 Oak: In front of you, there are three Pokémon. Each one has its own unique strengths:")
print(f"🧓 Oak:🔥 Charmander, with the fiery tail; 💧 Squirtle, the water-loving turtle; and 🌱 Bulbasaur, whose back grows a special plant.")
print(f"🧓 Oak: Choose wisely, as your choice will be your companion on this grand adventure!")

# I will store each Pokémon along with its color variable to keep the code clean. Additionally, I'll include their attacks, HP, levels, and the original damage each attack inflicts.

Ch = (f"{RED}Charmander{RESET}")
Ch_LvL = 5 ; Ch_HP = 48
Ch_attack1_name= "Ember" ; Ch_attack1_damage = 6
Ch_attack2_name= "Scratch" ; Ch_attack2_damage = 5
Ch_attack3_name= "Flamethrower" ; Ch_attack3_damage = 8
Ch_attack4_name= "Dragon Breath" ; Ch_attack4_damage = 7

Sq = (f"{BLUE}Squirtle{RESET}")
Sqspace = ("  ")
Sq_LvL = 5 ; Sq_HP = 50
Sq_attack1_name= "Water Gun" ; Sq_attack1_damage = 6
Sq_attack2_name= "Tackle" ; Sq_attack2_damage = 5
Sq_attack3_name= "Bubble" ; Sq_attack3_damage = 6
Sq_attack4_name= "Hydro Pump" ; Sq_attack4_damage = 8

Bu = (f"{GREEN}Bulbasaur{RESET}")
Buspace = (" ")
Bu_LvL = 5 ; Bu_HP = 49
Bu_attack1_name= "Vine Whip" ; Bu_attack1_damage = 6
Bu_attack2_name= "Headbutt" ; Bu_attack2_damage = 5
Bu_attack3_name= "Leech Seed" ; Bu_attack3_damage = 6
Bu_attack4_name= "Razor Leaf" ; Bu_attack4_damage = 7

#Graphic presentation in table format of the 3 Pokémon and their abilities
#I know this might bother perfectionists like me, but I have to leave it this way to print correctly the table in the log.
print(" ")
print(" ")
print(" ________________________________________________________________________") 
print(f"|   🔥 {Ch} 🔥   |   💧  {Sq}  💧{Sqspace}  |     🌱 {Bu}{Buspace}🌱     |")  
print("|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|")    
print(f"| 1. {Ch_attack1_name}              | 1. {Sq_attack1_name}         | 1. {Bu_attack1_name}            |")
print(f"| 2. {Ch_attack2_name}            | 2. {Sq_attack2_name}            | 2. {Bu_attack2_name}             |")
print(f"| 3. {Ch_attack3_name}       | 3. {Sq_attack3_name}            | 3. {Bu_attack3_name}           |")
print(f"| 4. {Ch_attack4_name}      | 4. {Sq_attack4_name}        | 4. {Bu_attack4_name}           |")
print("|_______________________|______________________|_________________________|")
print("")
print("")

# Now, the player will choose their starter Pokémon. I'll first create variables for the Pokémon and its attributes for each trainer. I use prfix "My" for the player and "Ga" for Gary pokemon. 
# I'll utilize a "while" loop to ensure the player picks a valid option (1, 2, or 3).
# will also determine which Pokémon Gary chooses based on the player's choice. (Always the strong Element Pokemon againts Player-s Pokemon)
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

#Until this point, the player hasn't been introduced to Gary; he's only been referenced in the previous lines of code. Let's infuse some backstory and drama to make the upcoming battle more exhilarating.
print(" __________________________________________________________________ ")
print(f"|{BWHITE}{BLACK}                                                                  {RESET}|")
print(f"|{BWHITE}{BLACK}  Now that you've made your choice, here's Gary! Remember him?    {RESET}|")
print(f"|{BWHITE}{BLACK}  He's Professor Oak's grandson and your lifelong rival in the    {RESET}|")
print(f"|{BWHITE}{BLACK}  world of Pokémon. He's never one to be outdone, so he's chosen  {RESET}|")
print(f"|{BWHITE}{BLACK}  his own starter Pokémon. Brace yourself; Gary challenges you    {RESET}|")
print(f"|{BWHITE}{BLACK}  to a battle right now to test the mettle of your new Pokémon!   {RESET}|")
print(f"|{BWHITE}__________________________________________________________________{RESET}|")
input(f"{ITALICS}>> Press [ENTER] to continue <<{RESET}")
print(" ")
print(f"😎 Gary: Heh, so you've chosen a {MyPokemon}, huh? It doesn't matter what you choose, because I'm always one step ahead!")
print("😎 Gary: There's a reason I'm the Professor's grandson. Get ready to see the difference between an amateur and a future Pokémon Champion!")
input(f"{ITALICS}>> Press [ENTER] to continue <<{RESET}")
print(F"😁 {PlayerName}: I'm always ready, Gary! Let the best trainer win!")
input(f"{ITALICS}>> Press [ENTER] to continue <<{RESET}")
print(" ")

print(" ____________________________________________________________________ ")
print(f"|{BWHITE}{BLACK}  🧓 Profesor Oak 🧓                                                {RESET}|")
print(f"|{BWHITE}{BLACK}  Wait just a moment, you two! Before you begin, I'm giving each    {RESET}|")
print(f"|{BWHITE}{BLACK}  of you some potions. Battles can be tough, and it's crucial to    {RESET}|")
print(f"|{BWHITE}{BLACK}  look after the well-being of your Pokémon. Don't push them to     {RESET}|")
print(f"|{BWHITE}{BLACK}  their limits without care. Remember, a good trainer always        {RESET}|")
print(f"|{BWHITE}{BLACK}  prioritizes the health and happiness of their Pokémon!            {RESET}|")
print(f"|{BWHITE}____________________________________________________________________{RESET}|")
print(f"{ITALICS}You store the potions in your inventory. Each one has a label stating it will heal up to 20 HP for your Pokémon.{RESET}")

input(f"{ITALICS}>> Press [ENTER] to continue <<{RESET}")
print(" ")

print("😎 Gary: Ready to learn how real Pokemon battle is done? Let's see if your Pokémon can stand up to mine!")
print (f"😎 Gary: Come on, {GaryPokemon}! {ITALICS}Gary has sent out {GaryPokemon}")
print(" ")
print(f"😁 {PlayerName}: Bring it on, Gary! I believe in my Pokémon, even if we've just started our journey together!")
print(f"😁 {PlayerName}: Come on, {MyPokemon}! {ITALICS}{PlayerName} have sent out {MyPokemon}")
print(" ")
input(f"{ITALICS}>> Press [ENTER] to continue <<{RESET}")


#Combat variables that I need to procees the combat, and let's add some emotions for our Pokemon, Some variables will be reset at the final of the big loop.

Action = 0             ; Turn = " "
emotion = 0

My_Top_HP = My_HP      ; 
My_HP_diff  = 0        ; Ga_HP_diff  = 0 
MychoosedAttack = " "  ; Myattackname = " "
Myattackdmg = 0

Ga_Top_HP = Ga_HP
Gaattackname = " "     ; GachooseAttack = " "
GachooseAttackdmg = " ";Gaattackdmg = 0
Objectselected = " "   ;Object1effect = 20






while My_HP != 0 and Ga_HP != 0:
    
    emotion = random.randint(1,5)
    if emotion == 1:
        emotion = ("Your Pokémon eagerly waits for you🐾 ❤️     ")
    elif emotion == 2:
        emotion = ("Your Pokémon is ready for action. 💪🔥     ")
    elif emotion == 3:
        emotion = ("Your Pokémon awaits your next move🧠🔍     ")
    elif emotion == 4:
        emotion = ("Your Pokémon is brimming with energy⚡🌀   ")
    elif emotion == 5:
        emotion = ("Your Pokémon stares with determination.👾🌟")
    else:
        emotion == ("Your Pokémon feels scared. 😨👻            ")


    #ident

    print(" __________________________________________________________ ")
    print("|                                                          |")
    if   GaryPokemon == Sq:
        print(f"| {GaryPokemon}{Sqspace}    Lv {Ga_LvL}                                       |")
    elif GaryPokemon == Ch:
        print(f"| {GaryPokemon}    Lv {Ga_LvL}                                       |")
    else: 
        print(f"| {GaryPokemon}{Buspace}    Lv {Ga_LvL}                                       |")     
    if Ga_HP < 10:
        print(f"| ❤️‍🩹  {Ga_HP} Hp                                                |")
    else:
        print(f"| ❤️  {Ga_HP} Hp                                                 |")    
    if   MyPokemon == Sq:
        print(f"|                                       {MyPokemon}{Sqspace}    Lv {My_LvL} |")
    elif MyPokemon == Ch:    
        print(f"|                                       {MyPokemon}    Lv {My_LvL} |")
    else:
        print(f"|                                       {MyPokemon}{Buspace}    Lv {My_LvL} |")  
    if My_HP < 10:
        print(f"|                                               ❤️‍🩹  {My_HP} Hp  |") 
    else:            
        print(f"|                                                 ❤️  {My_HP} Hp |")
    print("|__________________________________________________________| ")
    print(f"|{emotion}               {RESET}| ")
    if   MyPokemon == Sq:
        print(f"|What will {MyPokemon}{Sqspace} do?                                  | ")
    elif MyPokemon == Bu:
        print(f"|What will {MyPokemon}{Buspace} do?                                  | ")   
    else:      
        print(f"|What will {MyPokemon} do?                                  | ")

    Action=0   
    while Action != 1 and Action != 2 and Action != 3 and Action != 4 and Myattackname != " 1"  and Objectselected != " 1":
        print(f"|{BWHITE}{BLACK}                                                          {RESET}| ")
        print(f"|{BWHITE}{BLACK}    {RESET}{BOLDWHITE}1{RESET} Fight ⚔️  | {BOLDWHITE}2{RESET} Pokemon 🦁 |  {BOLDWHITE}3{RESET} Bag 👜  | {BOLDWHITE}4{RESET} Run🏃💨{BWHITE}{BLACK}    {RESET}| ")
        print(f"|{BWHITE}{BLACK}__________________________________________________________{RESET}| ")
        print(" ")
        Action = int(input(f"{ITALICS}Type your number option here: {RESET}"))
        print(" ")

        
        Ga_Random_Attack = 0   #por DESCRIBIR Esto
        Ga_Random_Attack = random.randint(1,5)
        Ga_fail = 0
        Ga_fail = random.randint(1,10)
        
        if   Ga_Random_Attack == 1:
            Gaattackname = Ga_attack1_name
            Gaattackdmg  = Ga_attack1_damage + 1
        elif Ga_Random_Attack  == 2:
            Gaattackname = Ga_attack2_name
            Gaattackdmg  = Ga_attack2_damage 
        elif Ga_Random_Attack  == 3:
            Gaattackname = Ga_attack3_name
            Gaattackdmg  = Ga_attack3_damage + 3    
        elif Ga_Random_Attack  == 4:
            Gaattackname = Ga_attack4_name
            Gaattackdmg  = Ga_attack4_damage + 4
        elif Ga_Random_Attack  == 5:
            if Ga_HP < 30:
                print("Print")
                Gaattackname = "Potion"
                Gaattackdmg  = 20 
            else:
                print(" control ", Ga_attack1_name )
                Gaattackname = Ga_attack1_name
                Gaattackdmg  = Ga_attack1_damage + 2

        if Action == 1:
            
            while MychoosedAttack != 1 and MychoosedAttack != 2 and MychoosedAttack != 3 and MychoosedAttack != 4 and MychoosedAttack != 0:
                print(f"           {BOLDBLUE}        ⚔️  Fight   Menu ⚔️{RESET}")
                print(" ")
                print("Type your attack or Type 0 to return to the main menu.")
                MychoosedAttack = int(input(f"{BOLDWHITE}→ 1{RESET} {My_attack1_name} {BOLDWHITE}→ 2{RESET} {My_attack2_name} {BOLDWHITE}→ 3{RESET} {My_attack3_name} {BOLDWHITE}→ 4{RESET} {My_attack4_name} "))
                RandomDamage = 0
                RandomDamage = random.randint(0,4)

                if  MychoosedAttack == 1:
                            Myattackname = My_attack1_name
                            Myattackdmg = My_attack1_damage + RandomDamage - 2
                elif  MychoosedAttack == 2:
                            Myattackname = My_attack2_name
                            Myattackdmg =  My_attack2_damage 
                elif  MychoosedAttack == 3:
                            Myattackname = My_attack3_name
                            Myattackdmg =  My_attack3_damage + RandomDamage
                    
                elif  MychoosedAttack == 4:
                            Myattackname = My_attack4_name
                            Myattackdmg =  My_attack4_damage + RandomDamage
                elif MychoosedAttack == 0:
                    Action = 0

            print(" ")       
            fails = 0
            fails = random.randint(0,10)
            Turn = random.randint(1,2)             

            if Turn == 1 and Action != 0:
                        print("Turno 1")        
                        print("============================================================")  
                        if  fails == 1 or fails == 3 or fails == 7:
                            print(f"{MyPokemon} used {BOLDWHITE}{Myattackname}{RESET}: but it failed!😲") 

                        else:
                            print(f"💥 {MyPokemon} used {BOLDWHITE}{Myattackname}{RESET}: {GaryPokemon} took {BOLDRED}{Myattackdmg}{RESET} damage!")
                            Ga_HP = Ga_HP - Myattackdmg      
                            if Ga_HP == Ga_HP <= 0:
                                Ga_HP = 0
                            print(f"🤕 {GaryPokemon} has {Ga_HP} HP left.")
                
                        if   Gaattackname != "Potion" and (Ga_fail == 1 or Ga_fail == 3 or Ga_fail == 7 or Ga_fail == 5):
                            print(f"{GaryPokemon} used {BOLDWHITE}{Gaattackname}{RESET}: but it failed!😲 ")    

                        elif Ga_fail >= 0  and  Ga_Random_Attack == 5:
                            Ga_HP = Ga_HP + Gaattackdmg 
                            if Ga_HP >= Ga_Top_HP:
                                Ga_HP_diff  = Ga_HP - Ga_Top_HP
                                Gaattackdmg = Gaattackdmg - Ga_HP_diff 
                                print(f"💊 {BOLDWHITE}Gary{RESET} used {BOLDWHITE}{Gaattackname}{RESET}! {GaryPokemon} recovered {BOLDGREEN}{Gaattackdmg}{RESET} ❤️   HP!")
                                Ga_HP =  Ga_Top_HP  

                        elif  Ga_fail == 2 or  Ga_fail == 4 or  Ga_fail == 6 or  Ga_fail == 8 or  Ga_fail == 9 or  Ga_fail == 10 and Ga_Random_Attack != 5:
                            print(f"💥 {GaryPokemon} used {BOLDWHITE}{Gaattackname}{RESET}: {MyPokemon} took {BOLDRED}{Gaattackdmg}{RESET} damage!")
                            My_HP = My_HP - Gaattackdmg      
                            if My_HP == My_HP <= 0:
                                My_HP = 0
                            print(f"🤕 {MyPokemon} has {My_HP} HP left.")                        
                            print("Action", Action)    
                        print("============================================================")
            elif Turn == 2 and Action != 0: 
                        print("Turno 2")
                        print("============================================================")
                        if  Gaattackname != "Potion" and  (Ga_fail == 1 or Ga_fail == 3 or Ga_fail == 7 or Ga_fail == 5):
                            print(f"{GaryPokemon} used {BOLDWHITE}{Gaattackname}{RESET}: but it failed!😲 ")   
                
                        elif Ga_fail >= 0  and  Ga_Random_Attack == 5:
                            Ga_HP = Ga_HP + Gaattackdmg 
                            if Ga_HP >= Ga_Top_HP:
                                Ga_HP_diff  = Ga_HP - Ga_Top_HP
                                Gaattackdmg = Gaattackdmg - Ga_HP_diff 
                                print(f"💊 {BOLDWHITE}Gary{RESET} used {BOLDWHITE}{Gaattackname}{RESET}! {GaryPokemon} recovered {BOLDGREEN}{Gaattackdmg}{RESET} ❤️   HP!")
                            Ga_HP =  Ga_Top_HP      

                        elif Ga_fail == 0 or Ga_fail == 2 or Ga_fail == 4  or Ga_fail ==  6 or Ga_fail == 8 or Ga_fail == 9 or Ga_fail == 10:
                            print(f"💥 {GaryPokemon} used {BOLDWHITE}{Gaattackname}{RESET}: {MyPokemon} took {BOLDRED}{Gaattackdmg}{RESET} damage!")
                            My_HP = My_HP - Gaattackdmg      
                            if My_HP == My_HP <= 0:
                                My_HP = 0
                            print(f"🤕 {MyPokemon} has {My_HP} left")

                        if fails == 1 or fails == 3 or fails == 7:
                            print(f"{MyPokemon} used {BOLDWHITE}{Myattackname}{RESET}: but it failed! 😲")    

                        elif fails == 0 or fails == 2 or fails == 4 or fails == 5 or fails == 6 or fails == 8 or fails == 9 or fails == 10:
                            print(f"💥 {MyPokemon} used {BOLDWHITE}{Myattackname}{RESET}: {GaryPokemon} took {BOLDRED}{Myattackdmg}{RESET} damage!")
                            Ga_HP = Ga_HP - Myattackdmg      
                            if Ga_HP == Ga_HP <= 0:
                                Ga_HP = 0
                            print(f"🤕 {GaryPokemon} has {Ga_HP} left") 
                        print("============================================================")
                        
                        

        elif Action == 2:

              print("No tienes otros Pokemon")
              print(" ")
              Action = 0

              
        elif Action == 3:
             
             while  Objectselected !=1 and Objectselected !=0:
              Objectselected = int(input(f"⚔️: {BOLDWHITE}→ 1{RESET} Potion "))
              print("Type your object or Type 0 to return to the main menu.")
              print(" ")
            
              if Objectselected == 0:
                   Action = 0
              elif Objectselected == 1:
                  
                  My_HP = My_HP + 20
                  
                  if My_HP >= My_Top_HP:
                     My_HP_diff  = My_HP - My_Top_HP
                   
                     My_HP = My_HP - 20
                     My_HP = My_HP + (20 - My_HP_diff)
                     
                     Object1effect = 20 - My_HP_diff
                     print("============================================================")
                     
                     
                     print(f"💊 {BOLDWHITE}{PlayerName}{RESET} used {BOLDWHITE}Potion{RESET}! {MyPokemon} recovered {BOLDGREEN}{Object1effect}{RESET} ❤️   HP!")
                     print(f"sumare a mi hp actual{My_HP} el diferencial{Object1effect}")
                  else:
                    print(f"💊 {BOLDWHITE}{PlayerName}{RESET} used {BOLDWHITE}Potion{RESET}! {MyPokemon} recovered {BOLDGREEN}20{RESET} ❤️   HP!")  
                    print("============================================================")

               
              if  Gaattackname != "Potion" and  (Ga_fail == 1 or Ga_fail == 3 or Ga_fail == 7 or Ga_fail == 5):
                     print(f"{GaryPokemon} used {BOLDWHITE}{Gaattackname}{RESET}: but it failed!😲 ")   
                
              elif Ga_fail >= 0  and  Ga_Random_Attack == 5:
                  Ga_HP = Ga_HP + Gaattackdmg 
                  if Ga_HP >= Ga_Top_HP:
                     Ga_HP_diff  = Ga_HP - Ga_Top_HP
                     Gaattackdmg = Gaattackdmg - Ga_HP_diff 
                     print(f"💊 {BOLDWHITE}Gary{RESET} used {BOLDWHITE}{Gaattackname}{RESET}! {GaryPokemon} recovered {BOLDGREEN}{Gaattackdmg}{RESET} ❤️   HP!")
                     Ga_HP =  Ga_Top_HP      

              elif Ga_fail == 0 or Ga_fail == 2 or Ga_fail == 4  or Ga_fail ==  6 or Ga_fail == 8 or Ga_fail == 9 or Ga_fail == 10:
                  print(f"💥 {GaryPokemon} used {BOLDWHITE}{Gaattackname}{RESET}: {MyPokemon} took {BOLDRED}{Gaattackdmg}{RESET} damage!")
                  My_HP = My_HP - Gaattackdmg      
                  if My_HP == My_HP <= 0:
                     My_HP = 0
                  print(f"🤕 {MyPokemon} has {My_HP} left")

              

                       
              print("============================================================") 
               
                 # if My_HP = My_Top_HP + 20 
                 #  Objectselected == "Potion"
                 #  if My_HP >= My_Top_HP:
                  #    My_HP = My_Top_HP
              
            #  print(f"💊 {BOLDWHITE}{PlayerName}{RESET} used {BOLDWHITE}Potion{RESET}! {MyPokemon} recovered {BOLDGREEN}{Gaattackdmg}{RESET} ❤️   HP!") 

             
         
        elif Action == 4:
               
               print("No puedes abandonar este combate")    
               Action = 0   
     
          
        MychoosedAttack = " "
        Myattackname = " "
        Myattackdmg = 0
        Objectselected = " "
        Turn = 0
        emotion = 0
        


          
         # input(f" {Objectselected},{My_HP} , {My_Top_HP} ?:")
print(" ")
  #  print(f"{MyPokemon} use {Myattackname}")
              
print("fin bucle")

    #print(f"{MyPokemon} use {Myattackname}: {GaryPokemon} lose {Myattackdmg}")
  
