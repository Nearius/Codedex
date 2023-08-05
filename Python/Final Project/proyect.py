import pygame, random, sys

# constants for the windows width and height values
SCREEN_WIDTH = 960
SCREEN_HEIGHT = 720

# the RGB values for the colors used in the game
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_CIAN = (0, 255, 255)

clock = pygame.time.Clock()

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Nearius World")
    icon = pygame.image.load('images/icon.png')
    pygame.display.set_icon(icon)
    started = False

    
    while True:
       if not started:
            font = pygame.font.SysFont('Consolas', 30)
            text = font.render('Bienvenidos a Nearius World', True, COLOR_WHITE)
            text_rect = text.get_rect()
            text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
            screen.blit(text, text_rect)
            pygame.display.flip()
            clock.tick(6)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
            if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_SPACE:
                  started = True

                
       screen.fill(COLOR_BLACK)  
       paddle_1_rect = pygame.Rect(30, SCREEN_HEIGHT // 2 - 50, 7, 100)
       paddle_2_rect = pygame.Rect(SCREEN_WIDTH - 50, SCREEN_HEIGHT // 2 - 50, 7, 100)
       ball_rect = pygame.Rect(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 25, 25)      
       paddle_1_rect = pygame.Rect(30, 0, 7, 100)
       paddle_2_rect = pygame.Rect(SCREEN_WIDTH - 50, 0, 7, 100)
       paddle_1_move = 0
       paddle_2_move = 0
       ball_rect = pygame.Rect(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 25, 25)
       ball_accel_x = random.randint(2, 4) * 0.1
       ball_accel_y = random.randint(2, 4) * 0.1

       if random.randint(1, 2) == 1:
           ball_accel_x *= -1
       if random.randint(1, 2) == 1:
           ball_accel_y *= -1
        
       pygame.draw.rect(screen, COLOR_WHITE, paddle_1_rect)
       pygame.draw.rect(screen, COLOR_WHITE, paddle_2_rect)

       pygame.draw.rect(screen, COLOR_CIAN, ball_rect)

       pygame.display.update()

       delta_time = clock.tick(60)


    # checking for events
       for event in pygame.event.get():

      # if the user exits the window
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit() 
        
       pygame.display.flip()

        # exit the function, to finish the game

main()
