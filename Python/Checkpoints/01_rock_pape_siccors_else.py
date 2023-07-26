# I import the random library to later assign a random number to the "computer" variable using .randint(),
import random

# First, I introduce myself and explain what this project is about. It's a mini-game, and before starting, I explain the rules:
print("Welcome to my very first project in Python, My name is Nearius, and I hope you enjoy it as much as I did writing this code.")
print("Let me introduce you to this game: Rock - Paper - Scissors - Lizard - Spock.")
print("A fun variation of the classic game Rock - Paper - Scissors." )
print("The rules are very similar to the ones from the classic, but with two new options, “Lizard” and “Spock”: ")
print(" ")
print('✌️  Scissors cut ✋ Paper.')
print('✋ Paper covers ✊ Rock.')
print('✊ Rock crushes 🦎 Lizard.')
print('🦎 Lizard poisons 🖖 Spock.')
print('🖖 Spock smashes ✌️  Scissors.')
print('✌️  Scissors beat 🦎 Lizard.')
print('🦎 Lizard eats ✋ Paper.')
print('✋ Paper disproves 🖖 Spock.')
print('🖖 Spock vaporizes ✊ Rock.')
print('✊ Rock breaks ✌️  Scissors')
print(" ")

# Next, there are several variables that I will use throughout the rest of the code.
player = 0
computer = random.randint(1,5)
player_choise = (' ')
computer_choise = (' ')
repeat = ("Yes")   
playervictories = 0
computervictories = 0
playername = input("Nickname: ")
print(" ")
print(f"Thanks you {playername}, let's start the game, good luck!")
print(" ")
#The game begins. The game will repeat over and over in this "while" loop as long as the player is not "Winner" and the repeat variable is not "No".

while player != ('winner') and repeat != ('No'):
    print("⭐=================================⭐")
    print("   Rock Paper Scissors Lizard Spock"   )
    print("⭐=================================⭐")
    print('1) ✊')
    print('2) ✋')
    print('3) ✌️')
    print('4) 🦎')
    print('5) 🖖')
    player = int(input("Pick a number betwen 1 - 5: "))
    print(" ")

    if player == 1:
        player_choise = ("✊")
    elif player == 2:
        player_choise = ("✋")
    elif player == 3:
        player_choise = ("✌️")
    elif player == 4:
        player_choise = ("🦎")
    elif player == 5:
        player_choise = ("🖖")
    elif player >= 6 or player == 0:
        player_choise = ("❌")
        print("❌ ⚠️ Wrong number ⚠️ ❌")
        print(" ")
    else:
        print(" Wrong number ☠️")
   

    if player_choise == ("❌"):
        computer_choise = ("❌")
    elif computer == 1:
        computer_choise = ("✊")
    elif computer == 2:
        computer_choise = ("✋")
    elif computer == 3:
        computer_choise = ("✌️")
    elif computer == 4:
        computer_choise = ("🦎")
    elif computer == 5:
        computer_choise = ("🖖")
    else:
        print("Wrong number ☠️")

    print("- Your choice: ", player_choise )    
    print("- CPU  choice: ", computer_choise)
    print(" ")
    
    

    if player_choise == ("❌") and computer_choise == ("❌"):
        print("Restarting the game. Remember to pick only a number between 1 and 5")
        print(" ")
        print(" ")
        computer = random.randint(1,5)    

    elif   player == computer:
        print("💥 Draw 💥")
        print(" ")
    
    elif player == 1 and computer == 2:
        print("🔴 You lose, Paper covers Rock. Try again! 🔴")
        print(" ")
        computervictories = computervictories + 1 
        computer = random.randint(1,5)
    elif player == 1 and computer == 5:
        print("🔴 You lose, Spock vaporizes Rock. Try again! 🔴")
        print(" ")
        computervictories = computervictories + 1 
        computer = random.randint(1,5)
    elif player == 2 and computer == 3:
        print("🔴 You lose, Scissors cut Paper. Try again! 🔴")
        print(" ")
        computervictories = computervictories + 1 
        computer = random.randint(1,5)
    elif player == 2 and computer == 4:
        print("🔴 You lose, Lizard eats Paper. Try again! 🔴")
        print(" ")
        computervictories = computervictories + 1 
        computer = random.randint(1,5)
    elif player == 3 and computer == 1:
        print("🔴 You lose, Rock breaks Scissors. Try again! 🔴")
        print(" ")
        computervictories = computervictories + 1 
        computer = random.randint(1,5)
    elif player == 3 and computer == 5:
        print("🔴 You lose, Spock smashes Scissors. Try again! 🔴")
        print(" ") 
        computervictories = computervictories + 1 
        computer = random.randint(1,5)
    elif player == 4 and computer == 1:
        print("🔴 You lose, Rock crushes Lizard. Try again! 🔴")
        print(" ") 
        computervictories = computervictories + 1 
        computer = random.randint(1,5)     
    elif player == 4 and computer == 3:
        print("🔴 You lose, Scissors beat Lizard. Try again! 🔴")
        print(" ") 
        computervictories = computervictories + 1 
        computer = random.randint(1,5)     
    elif player == 5 and computer == 4:
        print("🔴 You lose, Lizard poisons Spock. Try again! 🔴")
        print(" ") 
        computervictories = computervictories + 1 
        computer = random.randint(1,5)     
    elif player == 5 and computer == 2:
        print("🔴 You lose, Paper disproves Spock. Try again! 🔴")
        print(" ")
        computervictories = computervictories + 1  
        computer = random.randint(1,5)    
    else:
        player = ('winner')
        print('⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐')
        print(f'   {playername} won 🥳 ')
        print('⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐')

        print(" ")

        repeat = "wait"  #We are asking to repeat the game, with a loop to waranty the answer is Yes or No

        while repeat != ('Yes') and repeat != ('No'):
         repeat = input("You want to try again? Just Type [Yes] or [No]: ")
       
          
        player = 0
        playervictories = playervictories + 1
        computer = random.randint(1,5)


# Final score once the player doesn't want to continue
print("")
print(" ")
print(" 📊   S c o r e b o a r d   📊")
print("-------------------------------")
print(" ")
if playervictories == 1:
    print(f"{playername}: {playervictories} victory")
else:
    print(f"{playername}: {playervictories} victories")

if computervictories == 1:
   print(f"CPU: {computervictories} victory")
else:
    print(f"CPU: {computervictories} victories")
print(" ")
print(f"😄 Thank you for participating {playername} 😄")
print(" ")
     
