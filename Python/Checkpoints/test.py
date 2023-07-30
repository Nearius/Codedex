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
My_HP = 0
Ga_HP = 0
My_HP = int(input("My PH: "))
Ga_HP = int(input("Ga PH: "))


if   My_HP == 0 and Ga_HP == 0:            
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


input(f"{ITALICS}>> Press [ENTER] to continue <<{RESET}")   
print("                                                                        ...To be continued")  
