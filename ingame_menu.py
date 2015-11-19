import pygame
from pygame.locals import *

pygame.init()

dheight = 600
dwidth = 800

screen = pygame.display.set_mode((dwidth, dheight))
pygame.display.set_caption("Menu test")

screen.fill((255,255,255))

pygame.display.flip()

menu = pygame.Rect(10, 10, 50, 100)

running = True
MenuOpen = False

while running:
    screen.fill((255,255,255))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                MenuOpen = not MenuOpen
                
    if MenuOpen:
        pygame.draw.rect(screen, (0, 0, 255), (30, 30, 30, 30))


    pygame.display.update()

pygame.quit()