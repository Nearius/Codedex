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






#Here begins the large loop, and the goal of this project: To simulate a Pokémon battle in the style of the 
#early Game Boy games from the years 199x - 2000."

while My_HP != 0 and Ga_HP != 0:
    
    #Every time the loop restarts, our Pokémon will show an emotion. I thought of this feature to give the battle a bit more personality.
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

    #Below, we have the main combat panel, where the HP of each Pokémon is displayed, along with their level and name.
    #It will also show the emotion of the Pokémon we described earlier, and we have a panel available with four options.
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
    # We start the first inner loop, where we ensure that the player can only choose one of the 4 available options.
    while Action != 1 and Action != 2 and Action != 3 and Action != 4 and Myattackname != " 1"  and Objectselected != " 1":
        print(f"|{BWHITE}{BLACK}                                                          {RESET}| ")
        print(f"|{BWHITE}{BLACK}    {RESET}{BOLDWHITE}1{RESET} Fight ⚔️  | {BOLDWHITE}2{RESET} Pokemon 🦁 |  {BOLDWHITE}3{RESET} Bag 👜  | {BOLDWHITE}4{RESET} Run🏃💨{BWHITE}{BLACK}    {RESET}| ")
        print(f"|{BWHITE}{BLACK}__________________________________________________________{RESET}| ")
        print(" ")
        Action = int(input(f"{ITALICS}Type your number option here: {RESET}"))
        print(" ")

        #Now we determine which attack our opponent chooses and its probability of failure, using the random.randint tool.
        #I've designed it so that the enemy always chooses a Pokémon with a stronger type than mine. Therefore, I add a bit more attack damage to each move
        Ga_Random_Attack = 0 
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
        elif Ga_Random_Attack  == 5:      #If this condition is met, the opponent will use a potion to heal their Pokémon. Depending on the current HP level of the opponent, I allow them to use a potion or an attack.
            if Ga_HP < 45:
                Gaattackname = "Potion"
                Gaattackdmg  = 20 
            else:                
                Gaattackname = Ga_attack1_name
                Gaattackdmg  = Ga_attack1_damage + 2
                Ga_Random_Attack = 1

        if Action == 1:
            #Loop to ensure a correct option is chosen; otherwise, an option to return to the main menu is offered.
            while MychoosedAttack != 1 and MychoosedAttack != 2 and MychoosedAttack != 3 and MychoosedAttack != 4 and MychoosedAttack != 0:
                print(f"           {BOLDBLUE}        ⚔️  Fight   Menu ⚔️{RESET}")
                print(" ")
                print(f"{ITALICS}Type your attack or Type{RESET} {BOLDWHITE}0{RESET}{ITALICS} to return to the main menu.{RESET}")
                MychoosedAttack = int(input(f"{BOLDWHITE}→ 1{RESET} {My_attack1_name} {BOLDWHITE}→ 2{RESET} {My_attack2_name} {BOLDWHITE}→ 3{RESET} {My_attack3_name} {BOLDWHITE}→ 4{RESET} {My_attack4_name} "))
                RandomDamage = 0
                RandomDamage = random.randint(0,4)

                #These are the moves of our player's Pokémon. I've added a random.randint to make each attack diferent in every turn, but without much variation.
                if  MychoosedAttack == 1:
                            Myattackname = My_attack1_name
                            Myattackdmg = My_attack1_damage + RandomDamage - 2 #The first move is supposedly weaker, so I've added a nerf of -2 to it.
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
            fails = random.randint(0,10)  #Of course or Pokemon Can Fail his attack too and Ill control it with this variable
            Turn = random.randint(1,2)    # And also Who attack first will be controllet by this variable, no more boring battles alwais = .         

            #If you choose fight...
            if Turn == 1 and Action != 0:                               
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
                            print("Entramos en el area de cura del turno 1")
                            Ga_HP = Ga_HP + Gaattackdmg
                            if Ga_HP  >= Ga_Top_HP:
                                Ga_HP_diff  = Ga_HP - Ga_Top_HP
                                Gaattackdmg = Gaattackdmg - Ga_HP_diff                                
                                Ga_HP =  Ga_Top_HP  
                            print(f"💊 {BOLDWHITE}Gary{RESET} used {BOLDWHITE}{Gaattackname}{RESET}! {GaryPokemon} recovered {BOLDGREEN}{Gaattackdmg}{RESET} ❤️   HP!")
                                

                        elif  Ga_fail == 2 or  Ga_fail == 4 or  Ga_fail == 6 or  Ga_fail == 8 or  Ga_fail == 9 or  Ga_fail == 10 and Ga_Random_Attack != 5:
                            print(f"💥 {GaryPokemon} used {BOLDWHITE}{Gaattackname}{RESET}: {MyPokemon} took {BOLDRED}{Gaattackdmg}{RESET} damage!")
                            My_HP = My_HP - Gaattackdmg      
                            if My_HP == My_HP <= 0:
                                My_HP = 0
                            print(f"🤕 {MyPokemon} has {My_HP} HP left.")                        
                            print("Action", Action)    
                        print("============================================================")
            elif Turn == 2 and Action != 0:                        
                        print("============================================================")
                        if  Gaattackname != "Potion" and  (Ga_fail == 1 or Ga_fail == 3 or Ga_fail == 7 or Ga_fail == 5):
                            print(f"{GaryPokemon} used {BOLDWHITE}{Gaattackname}{RESET}: but it failed!😲 ")   
                
                        elif Ga_fail >= 0  and  Ga_Random_Attack == 5:
                            Ga_HP = Ga_HP + Gaattackdmg
                            if Ga_HP  >= Ga_Top_HP:
                                Ga_HP_diff  = Ga_HP - Ga_Top_HP
                                Gaattackdmg = Gaattackdmg - Ga_HP_diff                            
                                Ga_HP =  Ga_Top_HP 
                            print(f"💊 {BOLDWHITE}Gary{RESET} used {BOLDWHITE}{Gaattackname}{RESET}! {GaryPokemon} recovered {BOLDGREEN}{Gaattackdmg}{RESET} ❤️   HP!")                                  
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
                        
                        
        #If you try to swicht to another Pokemon... good try my friend :')
        elif Action == 2:

            print("You don't have other Pokémon to switch out.")
            print(" ")
            Action = 0

        #If you try to use an item, I've added a loop to ensure only available options are chosen. In this case, the player always uses the item before the opponent.
        elif Action == 3:

            while  Objectselected !=1 and Objectselected !=0:
                Objectselected = int(input(f"⚔️: {BOLDWHITE}→ 1{RESET} Potion "))
                print("Type your object or Type 0 to return to the main menu.")
                print(" ")
            
                if Objectselected == 0 or Objectselected >= 2:
                    Action = 0
                    

                elif Objectselected == 1 and Action == 3:

                    My_HP = My_HP + 20

                    if My_HP >= My_Top_HP:
                        My_HP_diff  = My_HP - My_Top_HP
                        My_HP = My_HP - 20
                        My_HP = My_HP + (20 - My_HP_diff)
                        Object1effect = 20 - My_HP_diff
                        print("============================================================")
                        print(f"💊 {BOLDWHITE}{PlayerName}{RESET} used {BOLDWHITE}Potion{RESET}! {MyPokemon} recovered {BOLDGREEN}{Object1effect}{RESET} ❤️   HP!")
                    
                    else:
                        print("============================================================")
                        print(f"💊 {BOLDWHITE}{PlayerName}{RESET} used {BOLDWHITE}Potion{RESET}! {MyPokemon} recovered {BOLDGREEN}20{RESET} ❤️   HP!")  
                
                if Action == 0:
                    print("")
                
                elif  Objectselected >=2:
                        print("")
                elif  Gaattackname != "Potion"  and ( Ga_fail == 1 or Ga_fail == 3 or Ga_fail == 7 or Ga_fail == 5):
                        print(f"{GaryPokemon} used {BOLDWHITE}{Gaattackname}{RESET}: but it failed!😲 ") 
                        print("============================================================")  
                
                elif Ga_fail >= 0  and  Ga_Random_Attack == 5 and Action == 3:
                    Ga_HP = Ga_HP + Gaattackdmg 
                    if Ga_HP  >= Ga_Top_HP:
                        Ga_HP_diff  = Ga_HP - Ga_Top_HP
                        Gaattackdmg = Gaattackdmg - Ga_HP_diff 
                        Ga_HP =  Ga_Top_HP  
                    print(f"💊 {BOLDWHITE}Gary{RESET} used {BOLDWHITE}{Gaattackname}{RESET}! {GaryPokemon} recovered {BOLDGREEN}{Gaattackdmg}{RESET} ❤️   HP!")       
                    print("============================================================")
                elif (Ga_fail == 0 or Ga_fail == 2 or Ga_fail == 4  or Ga_fail ==  6 or Ga_fail == 8 or Ga_fail == 9 or Ga_fail == 10) and Action == 3:
                    print(f"💥 {GaryPokemon} used {BOLDWHITE}{Gaattackname}{RESET}: {MyPokemon} took {BOLDRED}{Gaattackdmg}{RESET} damage!")
                    My_HP = My_HP - Gaattackdmg      
                    if My_HP == My_HP <= 0:
                        My_HP = 0
                    print(f"🤕 {MyPokemon} has {My_HP} left")
                    print("============================================================")

        #If players trys to avoid the battler or leave it..
        elif Action == 4:
            print("You cannot leave this battle.")    
            Action = 0   
        # Need to reset some Variables
        MychoosedAttack = " "
        Myattackname = " "
        Myattackdmg = 0
        Objectselected = " "
        Turn = 0
        emotion = 0
        

        

print(" ")
#Final part: once the large loop (which encompasses the entire battle) is completed and the health of one or both 
#Pokémon ends, we move on to the final part of the code where we write a brief conclusion based on the outcome of the battle.
if   My_HP == 0 and Ga_HP == 0:  
    print("============================================================")
    print(" ")
    print("Both Pokémon have been knocked out; the battle is declared a draw and cannot proceed further.")
    print(" ") 
    print("============================================================")         
    print(" ___________________________________________________________________ ")
    print(f"|{BWHITE}{BLACK}  🧓 Professor Oak 🧓                                              {RESET}|")
    print(f"|{BWHITE}{BLACK}  Astonishing! Both Pokémon have fallen at the same time!          {RESET}|")
    print(f"|{BWHITE}{BLACK}  In my years of studying Pokémon, rarely have I seen such a       {RESET}|")
    print(f"|{BWHITE}{BLACK}  balanced match. It's a tie!                                      {RESET}|")
    print(f"|{BWHITE}___________________________________________________________________{RESET}|")
    input(f"{ITALICS}>> Press [ENTER] to continue <<{RESET}")

    print(" ___________________________________________________________________ ")
    print(f"|{BWHITE}{BLACK}  🧓 Professor Oak 🧓                                              {RESET}|")
    print(f"|{BWHITE}{BLACK}  This just goes to show the potential both you and Gary possess.  {RESET}|")
    print(f"|{BWHITE}{BLACK}  Your journey has only just begun, and already you're showcasing  {RESET}|")
    print(f"|{BWHITE}{BLACK}  such prowess.                                                    {RESET}|")
    print(f"|{BWHITE}{BLACK}                                                                   {RESET}|")
    print(f"|{BWHITE}{BLACK}  Remember, the world of Pokémon is vast, filled with challenges   {RESET}|")
    print(f"|{BWHITE}{BLACK}  and adventures. I look forward to seeing how you both grow as    {RESET}|")
    print(f"|{BWHITE}{BLACK}  trainers. Till next time, and thank you for playing!             {RESET}|")
    print(f"|{BWHITE}___________________________________________________________________{RESET}|")
elif My_HP == 0 and Ga_HP != 0:
    print("============================================================")
    print(" ")
    print(f"{MyPokemon} has been knocked out! Battle concluded: Gary claims victory. ")
    print(" ") 
    print("============================================================") 
    print(" ____________________________________________________________________ ")
    print(f"|{BWHITE}{BLACK}  🧓 Professor Oak 🧓                                               {RESET}|")
    print(f"|{BWHITE}{BLACK}  It appears that your Pokémon has been defeated. Battles can be    {RESET}|")
    print(f"|{BWHITE}{BLACK}  tough, and this is just one of the many challenges you'll face    {RESET}|")
    print(f"|{BWHITE}{BLACK}  on your journey. Don't be disheartened; every trainer faces       {RESET}|")
    print(f"|{BWHITE}{BLACK}  defeat at some point.                                             {RESET}|")
    print(f"|{BWHITE}{BLACK}                                                                    {RESET}|")
    print(f"|{BWHITE}{BLACK}  Use this experience to learn and grow. Remember, bond with your   {RESET}|")
    print(f"|{BWHITE}{BLACK}  Pokémon, train harder, and approach your next battle with         {RESET}|")
    print(f"|{BWHITE}{BLACK}  renewed determination. The path to becoming a Pokémon Master      {RESET}|")
    print(f"|{BWHITE}{BLACK}  is filled with highs and lows. Stay resilient and never give up!  {RESET}|")
    print(f"|{BWHITE}____________________________________________________________________{RESET}|")

elif My_HP != 0 and Ga_HP == 0:
    print("============================================================")
    print(" ")
    print(f"{GaryPokemon} has been defeated! Battle concluded: {PlayerName} emerges as the victor.   ")
    print(" ") 
    print("============================================================") 
    print(" ____________________________________________________________________ ")
    print(f"|{BWHITE}{BLACK}  🧓 Professor Oak 🧓                                               {RESET}|")
    print(f"|{BWHITE}{BLACK}  Impressive work! Gary's Pokémon has been defeated. This shows     {RESET}|")
    print(f"|{BWHITE}{BLACK}  your potential and the strong bond you've started building with   {RESET}|")
    print(f"|{BWHITE}{BLACK}  your Pokémon. Keep up the good work!                              {RESET}|")
    print(f"|{BWHITE}{BLACK}                                                                    {RESET}|")
    print(f"|{BWHITE}{BLACK}  But remember, each battle is a learning experience for both       {RESET}|")
    print(f"|{BWHITE}{BLACK}  the winner and the loser. I'm sure Gary will come back even       {RESET}|")
    print(f"|{BWHITE}{BLACK}  stronger next time. Keep training and nurturing your Pokémon,     {RESET}|")
    print(f"|{BWHITE}{BLACK}  as the journey to becoming a Pokémon Master is long and filled    {RESET}|")
    print(f"|{BWHITE}{BLACK}  with many challenges. Great job today!                            {RESET}|")
    print(f"|{BWHITE}____________________________________________________________________{RESET}|")

    input(f"{ITALICS}>> Press [ENTER] to continue <<{RESET}")
    print(" ")
    print("😎 Gary: You may have won this round, but this isn't the last you'll see of me. Train hard, because next time, I won't go easy on you!")
    print(" ")

input(f"{ITALICS}>> Press [ENTER] to continue <<{RESET}")   
print("                                                                        ...To be continued")  
