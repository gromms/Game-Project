import pygame
import os
from pygame.locals import *
from menu_objects import *
import map_editor
import case_handler as ch
from monster_objects import *

pygame.init()

screen_x = 800
screen_y = 600

screen = pygame.display.set_mode((screen_x, screen_y))
screen.fill((0,255,255))
pygame.display.set_caption("Menu_tests")

pygame.display.flip()

case = {
    'Title Menu' : True,
    'Game Menu' : False,
    'Map Editor' : False
}

Title_Menu = Title_Menu(screen, case)
Game_Menu = Game_Menu(screen, case)
Map_Editor = Map_Editor(screen, screen_x, screen_y)
Mob_Slime = Mob_Slime(screen)

running = True

while running:   

    if case['Title Menu'] == True:
        Title_Menu.draw()
        Mob_Slime.loadImgs()

    if case['Game Menu'] == True:
        Game_Menu.draw()

    if case['Map Editor'] == True:
        Map_Editor.main()
        case.update(ch.updateDict(case, 'Title Menu'))



    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
            running = False

    pygame.display.flip()

    pygame.display.update()

pygame.quit()