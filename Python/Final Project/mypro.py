import pygame , sys
from pygame.locals import *

pygame.init()

#Screen - VENTANA   pasamos de Screen a screen
W, H = 750,450
Screen = pygame.display.set_mode ((W , H))
x = 0
FPS = 30
Clock = pygame.time.Clock()
pygame.display.set_caption('Nearius world 😁')
icon = pygame.image.load('images/icon.png')
pygame.display.set_icon(icon)

#Fondo
fondo = pygame.image.load('images/fondo.png').convert()
Oak = pygame.image.load('images/oak1.png')


#Paleta de colores
WHITE = (255,255,255)
GREEN = (0,0,255)
CYAN = (0,255,255)
BLUE = (0,0,255)
YELLOW = (255,255,0)
RED = (255,0,0)
PINK = (255,0,255)
BLACK = (0,0,0)


Textframe = pygame.draw.rect(Screen, BLACK, (18,327,712,108)) # primer marco de texto negro
pygame.draw.rect(Screen, WHITE, (24,332,700,98)) #segundo marco de texto blanco superpuesto
fuente = pygame.font.Font(None, 26) # Puedes ajustar el tamaño
textOak = fuente.render("Profesor Oak", True, BLUE)
text = fuente.render("¡Hey, Pokémon trainer!", True, BLACK) # Color blanco
text2 = fuente.render("Welcome to the world of Pokémon! I'm Professor Oak. Every Pokémon trainer starts", True, BLACK) # Color blanco
text3 = fuente.render("by choosing their very first Pokémon. Today, you get to make that choice. Will it be", True, BLACK) # Color blanco
text4 = fuente.render("the fiery Charmander, the water-loving Squirtle, or the plant-powered Bulbasaur?", True, BLACK) # Color blanco
text5 = fuente.render("But, Before you begin your journey, please tell me, what is your name?:", True, BLACK) # Color blanco
username = ""
text6 = " "# Color blanco
text7 = fuente.render("Now it's time to choose your first Pokemon ", True, BLACK) # Color blanco


def texbox():
    Textframe = pygame.draw.rect(Screen, BLACK, (18,327,712,108)) # primer marco de texto negro
    pygame.draw.rect(Screen, WHITE, (24,332,700,98)) #segundo marco de texto blanco superpuesto
    
def intro1():
    Screen.blit(Oak,(10,200))
    texbox()
    Screen.blit(text, (30, 338)) # Coordenadas para ubicar el texto dentro de la caja
    Screen.blit(text2, (30, 360)) # Coordenadas para ubicar el texto dentro de la caja
    Screen.blit(text3, (30, 380)) # Coordenadas para ubicar el texto dentro de la caja
    Screen.blit(text4, (30, 400)) # Coordenadas para ubicar el texto dentro de la caja

def intro2():
    Screen.blit(Oak,(10,200))
    texbox()
    Getusername = fuente.render(username, True, RED)  #Recogida datos jugador.    

    Screen.blit(textOak,(30,338))
    Screen.blit(text5, (30, 360))
    Screen.blit(Getusername, (30, 380)) # Coordenadas para ubicar el texto dentro de la caja

    

def intro3():
    Screen.blit(Oak,(10,200))
    texbox()
    text6 = fuente.render(f"Oh yes, {username} Now I remember you!", True, BLACK)
    Screen.blit(textOak,(30,338))
    Screen.blit(text6, (30, 360))
    Screen.blit(text7, (30, 380))

def pokemonpresentation():
    texbox()
    Leftframe = pygame.draw.rect(Screen, BLACK, (154,75,130,150)) # primer marco de texto negro
    pygame.draw.rect(Screen, WHITE, (25,15,85,85)) #segundo marco de texto blanco superpuesto
    



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
        
        #PARA RECOGER TEXTO DE Screen
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                username = username[:-1]
            else:
                username += event.unicode

    #FONDO DE Screen EN MOVIMIENTO.       
    x_relative = x % fondo.get_rect().width    
    Screen.blit(fondo,(x_relative - fondo.get_rect().width , 0))  
    if x_relative < W:
        Screen.blit(fondo, (x_relative, 0))
    x -= 1    

    pokemonpresentation()

    if state == "intro1":   #control what we see on screen
        intro1() 
        frame1 = draw_button(Screen, "Next", 645, 295, 60, 35, BLACK)  
        button_rect = draw_button(Screen, "Next", 650, 300, 50, 25, WHITE)   #Botton  para cambiar de escena
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()
        if button_rect.collidepoint(mouse_pos) and mouse_pressed[0]:
            state = "intro2"
            pygame.time.wait(500) 
        

    elif state == "intro2":
        intro2()
        frame2 = draw_button(Screen, "Next", 645, 295, 60, 35, BLACK)  
        button_rect = draw_button(Screen, "Next", 650, 300, 50, 25, WHITE)   #PROBLEMA, AL PULSAR EL BOTON PREVIO, AQUI PASAMOS A LA 3 INTRO RAPIDO.
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()
        if button_rect.collidepoint(mouse_pos) and mouse_pressed[0]:
            state = "intro3"
            pygame.time.wait(500) 

    elif state == "intro3":
        intro3()



    
    pygame.display.update()       
    Clock.tick(FPS)