import pygame
import os
from pygame.locals import *
from menu_objects import *

pygame.init()

screen_x = 800
screen_y = 600

screen = pygame.display.set_mode((screen_x, screen_y))
screen.fill((0,255,255))
pygame.display.set_caption("Menu_tests")

pygame.display.flip()

Title_Menu = Title_Menu(screen)
Game_Menu = Game_Menu(screen)

Title_Menu_dif = True
Game_Menu_dif = False
running = True

while running:

    
    

    if Title_Menu_dif:
        Title_Menu.draw()

    if Game_Menu_dif:
        Game_Menu.draw()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
            running = False

    pygame.display.flip()

    pygame.display.update()

pygame.quit()