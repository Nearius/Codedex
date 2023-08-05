import pygame
import random
import sys
# constants for the windows width and height values
SCREEN_WIDTH = 960
SCREEN_HEIGHT = 720

# the RGB values for the colors used in the game
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)


def main():
# GAME SETUP

  #  initialize the PyGame library (this is absolutely necessary)
    pygame.init()
    screen = pygame.display.set_mode((900,600))
    while True:
        
        pygame.display.set_caption("Nearius World")
        icon = pygame.image.load('images/icon.png')
        pygame.display.set_icon(icon)
        screen.fill(COLOR_BLACK)

    # checking for events
        for event in pygame.event.get():

      # if the user exits the window
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit() 
        
        pygame.display.flip()

        # exit the function, to finish the game

main()
