import pygame , sys
from pygame.locals import *

pygame.init()

PANTALLA = pygame.display.set_mode ((750 , 450))
pygame.display.set_caption('Nearius world 😁')
icon = pygame.image.load('images/icon.png')
pygame.display.set_icon(icon)
fondo = pygame.image.load('images/pixel.jpg')
Oak = pygame.image.load('images/oak1.png')

#colores:

WHITE = (255,255,255)
GREEN = (0,0,255)
CYAN = (0,255,255)
BLUE = (0,0,255)
YELLOW = (255,255,0)
RED = (255,0,0)
PINK = (255,0,255)
BLACK = (0,0,0)

#PANTALLA.fill(BLACK)
PANTALLA.blit(fondo,(0,-20))
PANTALLA.blit(Oak,(10,200))

Textframe = pygame.draw.rect(PANTALLA, BLACK, (18,327,712,108))
pygame.draw.rect(PANTALLA, WHITE, (24,332,700,98))
fuente = pygame.font.Font(None, 26) # Puedes ajustar el tamaño
text = fuente.render("¡Hey, Pokémon trainer!", True, BLACK) # Color blanco
text2 = fuente.render("Welcome to the world of Pokémon! I'm Professor Oak...I should Continue?", True, BLACK) # Color blanco
PANTALLA.blit(text, (30, 338)) # Coordenadas para ubicar el texto dentro de la caja
PANTALLA.blit(text2, (30, 360)) # Coordenadas para ubicar el texto dentro de la caja
#Bucle del Juego
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.ecit()
    pygame.display.update()       