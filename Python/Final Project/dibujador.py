import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((750, 450))

drawing = False
rect_start = (0, 0)
rect_end = (0, 0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            rect_start = pygame.mouse.get_pos()
            drawing = True
        elif event.type == pygame.MOUSEBUTTONUP:
            rect_end = pygame.mouse.get_pos()
            drawing = False
            width = rect_end[0] - rect_start[0]
            height = rect_end[1] - rect_start[1]
            print(f"Rectángulo: (x={rect_start[0]}, y={rect_start[1]}), (ancho={width}, alto={height})")

    screen.fill((255, 255, 255))

    if drawing:
        rect_end = pygame.mouse.get_pos()
        pygame.draw.rect(screen, (0, 0, 0), (*rect_start, rect_end[0] - rect_start[0], rect_end[1] - rect_start[1]), 1)

    pygame.display.flip()