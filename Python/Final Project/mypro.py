import pygame , sys
from pygame.locals import *

pygame.init()

#PANTALLA - VENTANA
W, H = 750,450
PANTALLA = pygame.display.set_mode ((W , H))
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


#PANTALLA.fill(BLACK)

PANTALLA.blit(Oak,(10,200))

Textframe = pygame.draw.rect(PANTALLA, BLACK, (18,327,712,108)) # primer marco de texto negro
pygame.draw.rect(PANTALLA, WHITE, (24,332,700,98)) #segundo marco de texto blanco superpuesto
fuente = pygame.font.Font(None, 26) # Puedes ajustar el tamaño
text = fuente.render("¡Hey, Pokémon trainer!", True, BLACK) # Color blanco
text2 = fuente.render("Welcome to the world of Pokémon! I'm Professor Oak. Every Pokémon trainer starts", True, BLACK) # Color blanco
text3 = fuente.render("by choosing their very first Pokémon. Today, you get to make that choice. Will it be", True, BLACK) # Color blanco
text4 = fuente.render("the fiery Charmander, the water-loving Squirtle, or the plant-powered Bulbasaur?", True, BLACK) # Color blanco
text5 = fuente.render("Pero primero, puedes decirme tu nombre?", True, BLACK) # Color blanco
username = " "
text6 = fuente.render(f"Ha, {username} ahora te recuerdo bien.", True, BLACK) # Color blanco

PANTALLA.blit(text, (30, 338)) # Coordenadas para ubicar el texto dentro de la caja
PANTALLA.blit(text2, (30, 360)) # Coordenadas para ubicar el texto dentro de la caja


def texbox():
    Textframe = pygame.draw.rect(PANTALLA, BLACK, (18,327,712,108)) # primer marco de texto negro
    pygame.draw.rect(PANTALLA, WHITE, (24,332,700,98)) #segundo marco de texto blanco superpuesto
    
def intro1():
    PANTALLA.blit(Oak,(10,200))
    texbox()
    PANTALLA.blit(text, (30, 338)) # Coordenadas para ubicar el texto dentro de la caja
    PANTALLA.blit(text2, (30, 360)) # Coordenadas para ubicar el texto dentro de la caja
    PANTALLA.blit(text3, (30, 380)) # Coordenadas para ubicar el texto dentro de la caja
    PANTALLA.blit(text4, (30, 400)) # Coordenadas para ubicar el texto dentro de la caja

def intro2():
    PANTALLA.blit(Oak,(10,200))
    texbox()

    PANTALLA.blit(text5, (30, 338))

    Getusername = fuente.render(username, True, RED)  #Recogida datos jugador.
    PANTALLA.blit(Getusername, (30, 360)) # Coordenadas para ubicar el texto dentro de la caja
    

def intro3():
    PANTALLA.blit(Oak,(10,200))
    texbox()

    PANTALLA.blit(text6, (30, 338)) # Coordenadas para ubicar el texto dentro de la caja



def draw_button(screen, text, x, y, w, h, color):
    # Dibuja un rectángulo que será nuestro botón
    button_rect = pygame.draw.rect(screen, color, (x, y, w, h))

    # Crea una fuente y renderiza el texto que irá en el botón
    font = pygame.font.Font(None, 24)
    text_surf = font.render(text, True, BLACK)  # el color del texto será negro
    text_rect = text_surf.get_rect()
    text_rect.center = ((x+(w/2)), (y+(h/2)))  # centra el texto en el botón

    # Dibuja el texto en la pantalla
    screen.blit(text_surf, text_rect)

    return button_rect




state = "intro1"

#Bucle del Juego
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        
        #PARA RECOGER TEXTO DE PANTALLA
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                username = username[:-1]
            else:
                username += event.unicode

    #FONDO DE PANTALLA EN MOVIMIENTO.       
    x_relative = x % fondo.get_rect().width    
    PANTALLA.blit(fondo,(x_relative - fondo.get_rect().width , 0))  
    if x_relative < W:
        PANTALLA.blit(fondo, (x_relative, 0))
    x -= 1    



    if state == "intro1":   #control what we see on screen
        intro1() 

        button_rect = draw_button(PANTALLA, "Next", 650, 300, 50, 25, WHITE)   #Botton  para cambiar de escena
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()
        if button_rect.collidepoint(mouse_pos) and mouse_pressed[0]:
            state = "intro2"

    elif state == "intro2":
        intro2() 
        button_rect = draw_button(PANTALLA, "Next", 350, 300, 50, 25, WHITE)   #PROBLEMA, AL PULSAR EL BOTON PREVIO, AQUI PASAMOS A LA 3 INTRO RAPIDO.
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()
        if button_rect.collidepoint(mouse_pos) and mouse_pressed[0]:
            state = "intro3"

    elif state == "intro3":
        intro3()



    
    pygame.display.update()       
    Clock.tick(FPS)