import pygame , sys
from pygame.locals import *



#==================== Main Screen AND Global variables====================
pygame.init()
W, H = 750,450
Screen = pygame.display.set_mode ((W , H))
x = 0
FPS = 30
Clock = pygame.time.Clock()
pygame.display.set_caption('Nearius world 😁')
icon = pygame.image.load('images/icon.png')
pygame.display.set_icon(icon)
fondo = pygame.image.load('images/fondo.png').convert()   #Fondo means Background in Spanish
hide_pokeballs = False


#====================SPRITES====================
Oak = pygame.image.load('images/oak1.png')
Pokeball = pygame.image.load('images/pokeball.png')
CHPokeball = pygame.image.load('images/pokeball.png')
SQPokeball = pygame.image.load('images/pokeball.png')
BUPokeball = pygame.image.load('images/pokeball.png')
Charmander = pygame.image.load('images/charmander1.png')
Squirtle = pygame.image.load('images/squirtle.png')
Bulbasaur = pygame.image.load('images/bulbasaur.png')


#====================🌈COLORS🌈====================

WHITE = (255,255,255)
GREEN = (0,0,255)
CYAN = (0,255,255)
BLUE = (0,0,255)
YELLOW = (255,255,0)
RED = (255,0,0)
PINK = (255,0,255)
BLACK = (0,0,0)

#====================TEXTS====================

fuente = pygame.font.Font(None, 26) # Puedes ajustar el tamaño
textOak = fuente.render("Profesor Oak", True, BLUE)
text = fuente.render("¡Hey, Pokémon trainer!", True, BLACK)
text2 = fuente.render("Welcome to the world of Pokémon! I'm Professor Oak. Every Pokémon trainer starts", True, BLACK) 
text3 = fuente.render("by choosing their very first Pokémon. Today, you get to make that choice. Will it be", True, BLACK) 
text4 = fuente.render("the fiery Charmander, the water-loving Squirtle, or the plant-powered Bulbasaur?", True, BLACK)
text5 = fuente.render("But, Before you begin your journey, please tell me, what is your name?:", True, BLACK) 
username = ""
text6 = " "# Color blanco
text7 = fuente.render("Now it's time to choose your first Pokemon ", True, BLACK) 

#==============SPRITES MOVEMENTS============

#Charmander Pokeball
coord_CHpokeball_x = 187  
coord_CHpokeball_y = 137

speed_CH_x = -3
speed_CH_y = 3

#Squirtle Pokeball
coord_SQpokeball_x = 375  
coord_SQpokeball_y = 137

speed_SQ_x = 3
speed_SQ_y = -3 

#Bulbasaur Pokeball
coord_BUpokeball_x = 562
coord_BUpokeball_y = 137

speed_BU_x = 3
speed_BU_y = 3 

#====================Functions====================

#This function places a text frame at the bottom of the screen and controls the appearance of the Poké Balls spinning randomly until one of them is selected.
def texbox():
    Textframe = pygame.draw.rect(Screen, BLACK, (18,327,712,108)) 
    pygame.draw.rect(Screen, WHITE, (24,332,700,98)) 


    if not hide_pokeballs:
        Screen.blit(CHPokeball, (coord_CHpokeball_x,coord_CHpokeball_y))
        Screen.blit(SQPokeball, (coord_SQpokeball_x,coord_SQpokeball_y))
        Screen.blit(BUPokeball, (coord_BUpokeball_x,coord_BUpokeball_y))
    
# The functions intro1 / intro2 / intro3 will add text to the text box created in the texbox() function.    
def intro1():
    Screen.blit(Oak,(10,200))
    texbox()
    Screen.blit(text, (30, 338)) 
    Screen.blit(text2, (30, 360)) 
    Screen.blit(text3, (30, 380)) 
    Screen.blit(text4, (30, 400)) 
def intro2():
    Screen.blit(Oak,(10,200))
    texbox()
    Getusername = fuente.render(username, True, RED)  #Gets player name.  
    Screen.blit(textOak,(30,338))
    Screen.blit(text5, (30, 360))
    Screen.blit(Getusername, (30, 380)) 

def intro3():
    Screen.blit(Oak,(10,200))
    texbox()
    text6 = fuente.render(f"Oh yes, {username} Now I remember you!", True, BLACK)
    Screen.blit(textOak,(30,338))
    Screen.blit(text6, (30, 360))
    Screen.blit(text7, (30, 380))

#This function will control the movement of the 3 pokeballs on the initial screen; I must import the variables with the Global keyword.
def pokemove(): 
    global  speed_x, speed_y, coord_CHpokeball_x, coord_CHpokeball_y,speed_CH_x,speed_CH_y, coord_SQpokeball_x, coord_SQpokeball_y,speed_SQ_x,speed_SQ_y,coord_BUpokeball_x, coord_BUpokeball_y,speed_BU_x,speed_BU_y  #Keyword "global" para acceder y modificar variables globales.


#charmander
    if (coord_CHpokeball_x > 720 or coord_CHpokeball_x < 0):
        speed_CH_x *= -1
    if (coord_CHpokeball_y > 300 or coord_CHpokeball_y < 0):
        speed_CH_y *= -1

    coord_CHpokeball_x += speed_CH_x
    coord_CHpokeball_y += speed_CH_y

#Squirtle
    if (coord_SQpokeball_x > 720 or coord_SQpokeball_x < 0):
        speed_SQ_x *= -1
    if (coord_SQpokeball_y > 300 or coord_SQpokeball_y < 0):
        speed_SQ_y *= -1

    coord_SQpokeball_x += speed_SQ_x
    coord_SQpokeball_y += speed_SQ_y

#Burbasaur
    if (coord_BUpokeball_x > 720 or coord_BUpokeball_x < 0):
        speed_BU_x *= -1
    if (coord_BUpokeball_y > 300 or coord_BUpokeball_y < 0):
        speed_BU_y *= -1

    coord_BUpokeball_x += speed_BU_x
    coord_BUpokeball_y += speed_BU_y


#Thanks to this function, once it reaches intro 3, the 3 pokeballs will move to the center of the screen and shake until one of them is chosen.
def finalpokebal():
    global coord_CHpokeball_y, coord_CHpokeball_x, coord_SQpokeball_y, coord_SQpokeball_x, coord_BUpokeball_y, coord_BUpokeball_x

#Charmander
    if coord_CHpokeball_y > 137:
        coord_CHpokeball_y = coord_CHpokeball_y - 3
    elif coord_CHpokeball_y < 137:
        coord_CHpokeball_y = coord_CHpokeball_y + 3       

    if coord_CHpokeball_x > 187:
        coord_CHpokeball_x = coord_CHpokeball_x - 4
    elif coord_CHpokeball_x < 187:
        coord_CHpokeball_x = coord_CHpokeball_x + 4
    
#Squirtle
    if coord_SQpokeball_y > 137:
        coord_SQpokeball_y = coord_SQpokeball_y - 3
    elif coord_SQpokeball_y < 137:
        coord_SQpokeball_y = coord_SQpokeball_y + 3       

    if coord_SQpokeball_x > 375:
        coord_SQpokeball_x = coord_SQpokeball_x - 4
    elif coord_CHpokeball_x < 375:
        coord_SQpokeball_x = coord_SQpokeball_x + 4
    
#Bulbasaur
    if coord_BUpokeball_y > 137:
        coord_BUpokeball_y = coord_BUpokeball_y - 3
    elif coord_BUpokeball_y < 137:
        coord_BUpokeball_y = coord_BUpokeball_y + 3       

    if coord_BUpokeball_x > 562:
        coord_BUpokeball_x = coord_BUpokeball_x - 4
    elif coord_CHpokeball_x < 562:
        coord_BUpokeball_x = coord_BUpokeball_x + 4
    
    Clock.tick(50)



#This has been the most complicated of all the functions for me. Once a pokeball is chosen, it will move to the center of the screen to display an image of the selected Pokémon, while the remaining pokeballs will move off the screen.
def choosedpokeball():
    global coord_CHpokeball_y, coord_CHpokeball_x, coord_SQpokeball_y, coord_SQpokeball_x, coord_BUpokeball_y, coord_BUpokeball_x, state, Charmander, Squirtle, Bulbasaur, hide_pokeballs

    selected_pokemon = state
    target_x, target_y = 375, 137

    def move_to_target(coord_x, coord_y, target_x, target_y, speed_x=4, speed_y=3):
        if coord_y > target_y:
            coord_y = max(coord_y - speed_y, target_y)
        elif coord_y < target_y:
            coord_y = min(coord_y + speed_y, target_y)

        if coord_x > target_x:
            coord_x = max(coord_x - speed_x, target_x)
        elif coord_x < target_x:
            coord_x = min(coord_x + speed_x, target_x)

        return coord_x, coord_y
    

#show the pokemon selected
    def show_the_pokemon(pokemon):
        global coord_CHpokeball_y
        if pokemon == "selected_charmander":
            Screen.blit(Charmander, (300,60))             
        elif pokemon == "selected_squirtle":
            Screen.blit(Squirtle, (300,60))         
        elif pokemon == "selected_bulbasaur":
            Screen.blit(Bulbasaur, (300,60))


    # We quickly move the selected Pokeball toward the center.
    if selected_pokemon == "selected_charmander":
        coord_CHpokeball_x, coord_CHpokeball_y = move_to_target(coord_CHpokeball_x, coord_CHpokeball_y, target_x, target_y)

        if coord_CHpokeball_x == target_x and coord_CHpokeball_y == target_y:
            show_the_pokemon(selected_pokemon)
            hide_pokeballs = True

        coord_SQpokeball_x, coord_SQpokeball_y = move_to_target(coord_SQpokeball_x, coord_SQpokeball_y, -100, -100, speed_x=6, speed_y=6)
        coord_BUpokeball_x, coord_BUpokeball_y = move_to_target(coord_BUpokeball_x, coord_BUpokeball_y, 850, -100, speed_x=6, speed_y=6)

    elif selected_pokemon == "selected_squirtle":
        coord_SQpokeball_x, coord_SQpokeball_y = move_to_target(coord_SQpokeball_x, coord_SQpokeball_y, target_x, target_y)
        if coord_SQpokeball_x == target_x and coord_SQpokeball_y == target_y:
            show_the_pokemon(selected_pokemon)
            hide_pokeballs = True

        coord_CHpokeball_x, coord_CHpokeball_y = move_to_target(coord_CHpokeball_x, coord_CHpokeball_y, -100, -100, speed_x=6, speed_y=6)
        coord_BUpokeball_x, coord_BUpokeball_y = move_to_target(coord_BUpokeball_x, coord_BUpokeball_y, 850, -100, speed_x=6, speed_y=6)

    elif selected_pokemon == "selected_bulbasaur":
        coord_BUpokeball_x, coord_BUpokeball_y = move_to_target(coord_BUpokeball_x, coord_BUpokeball_y, target_x, target_y)
        if coord_BUpokeball_x == target_x and coord_BUpokeball_y == target_y:
            show_the_pokemon(selected_pokemon)
            hide_pokeballs = True

        coord_SQpokeball_x, coord_SQpokeball_y = move_to_target(coord_SQpokeball_x, coord_SQpokeball_y, -100, -100, speed_x=6, speed_y=6)
        coord_CHpokeball_x, coord_CHpokeball_y = move_to_target(coord_CHpokeball_x, coord_CHpokeball_y, 850, -100, speed_x=6, speed_y=6)



def draw_button(screen, text, x, y, w, h, color):
    # Dibuja un rectángulo que será nuestro botón
    button_rect = pygame.draw.rect(screen, color, (x, y, w, h))

    # Crea una fuente y renderiza el texto que irá en el botón
    font = pygame.font.Font(None, 24)
    text_surf = font.render(text, True, BLACK)  # el color del texto será negro
    text_rect = text_surf.get_rect()
    text_rect.center = ((x+(w/2)), (y+(h/2)))  # centra el texto en el botón

    # Dibuja el texto en la Screen
    Screen.blit(text_surf, text_rect)

    return button_rect



state = "intro1"

#Bucle del Juego
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        
#TAKE INPUTS FROM USERNAME
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                username = username[:-1]
            else:
                username += event.unicode
# IMAGES MOVEMENT  
            


#FONDO DE Screen EN MOVIMIENTO.       
    x_relative = x % fondo.get_rect().width    
    Screen.blit(fondo,(x_relative - fondo.get_rect().width , 0))  
    if x_relative < W:
        Screen.blit(fondo, (x_relative, 0))
    x -= 1    


    if state == "intro1":   #states control what we see on screen
        intro1() 
        pokemove() 
        frame1 = draw_button(Screen, "Next", 645, 295, 60, 35, BLACK)  
        button_rect = draw_button(Screen, "Next", 650, 300, 50, 25, WHITE)   #Botton  para cambiar de escena
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()
        if button_rect.collidepoint(mouse_pos) and mouse_pressed[0]:
            state = "intro2"
            pygame.time.wait(500) 
        

    elif state == "intro2":
        intro2()
        pokemove()
        frame2 = draw_button(Screen, "Next", 645, 295, 60, 35, BLACK)  
        button_rect = draw_button(Screen, "Next", 650, 300, 50, 25, WHITE)   
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()
        if button_rect.collidepoint(mouse_pos) and mouse_pressed[0]:
            state = "intro3"
            pygame.time.wait(500) 

    elif state == "intro3":
        intro3()
        finalpokebal()

        charmander_rect = pygame.Rect(coord_CHpokeball_x, coord_CHpokeball_y, CHPokeball.get_width(), CHPokeball.get_height())
        squirtle_rect = pygame.Rect(coord_SQpokeball_x, coord_SQpokeball_y, SQPokeball.get_width(), SQPokeball.get_height())
        bulbasaur_rect = pygame.Rect(coord_BUpokeball_x, coord_BUpokeball_y, BUPokeball.get_width(), BUPokeball.get_height())

        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()

        if charmander_rect.collidepoint(mouse_pos) and mouse_pressed[0]:
            state = "selected_charmander"
            pygame.time.wait(500)

        elif squirtle_rect.collidepoint(mouse_pos) and mouse_pressed[0]:
            state = "selected_squirtle"
            pygame.time.wait(500)

        elif bulbasaur_rect.collidepoint(mouse_pos) and mouse_pressed[0]:
            state = "selected_bulbasaur"
            pygame.time.wait(500)
    
    elif state == "selected_charmander":
            choosedpokeball()
            texbox()
            selected_text = fuente.render(f"Congratulations, {username}! You've chosen Charmander!", True, RED)
            Screen.blit(selected_text, (30, 360))


    elif state == "selected_squirtle":
            choosedpokeball()
            texbox()
            selected_text = fuente.render(f"Congratulations, {username}! You've chosen Squirtle!", True, BLUE)
            Screen.blit(selected_text, (30, 360))
    
    elif state == "selected_bulbasaur":
            choosedpokeball()
            texbox()
            selected_text = fuente.render(f"Congratulations, {username}! You've chosen Bulbasaur!", True, GREEN)
            Screen.blit(selected_text, (30, 360))

        


    Clock.tick(FPS)


    
    pygame.display.update()       
    Clock.tick(FPS)