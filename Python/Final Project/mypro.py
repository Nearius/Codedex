import pygame , sys
from pygame.locals import *

pygame.init()

#PANTALLA - VENTANA
W, H = 750,450
PANTALLA = pygame.display.set_mode ((W , H))
x = 0
FPS = 30
Clock = pygame.time.Clock()
#Icono y titulo de la ventana
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
text2 = fuente.render("Welcome to the world of Pokémon! I'm Professor Oak...I should Continue?", True, BLACK) # Color blanco

PANTALLA.blit(text, (30, 338)) # Coordenadas para ubicar el texto dentro de la caja
PANTALLA.blit(text2, (30, 360)) # Coordenadas para ubicar el texto dentro de la caja

#Bucle del Juego
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
    x_relative = x % fondo.get_rect().width    
    PANTALLA.blit(fondo,(x_relative - fondo.get_rect().width , 0))  
    if x_relative < W:
        PANTALLA.blit(fondo, (x_relative, 0))
    x -= 1    
    pygame.display.update()       
    Clock.tick(FPS)