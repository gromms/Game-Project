import pygame
import os
from pygame.locals import *

class Mob_Slime(pygame.sprite.Sprite):

    def __init__(self, screen):

        self.screen = screen

        self.screen_x = 800
        self.screen_y = 600

        self.Slime_Sheet = pygame.image.load("./Imgs/slime/slime_spritesheet.png").convert_alpha()

        self.slimeF_counter = 0

        self.slimeF_x = 0

        self.Slime_speed = 3

        self.clock = pygame.time.Clock()

    def draw(self, direction, x, y):
        #limit = self.clock.tick(60)
        x = x*40
        y = y*40

        if direction == "L":
            self.slimeF_x = 80
            if self.slimeF_x < 120:
                self.Slime_Sheet.set_clip(pygame.Rect(self.slimeF_x, 0, 40, 40))
                draw_Slime = self.Slime_Sheet.subsurface(self.Slime_Sheet.get_clip())
                self.screen.blit(draw_Slime, pygame.Rect(x, y, 800, 600))
                pygame.display.update()
                self.slimeF_counter += 1

                pygame.display.update()

                self.slimeF_x += 40

                if self.slimeF_x == 120 and self.slimeF_counter >= 120 and self.slimeF_counter <= 240:
                    self.Slime_Sheet.set_clip(pygame.Rect(self.slimeF_x, 0, 40, 40))
                    draw_Slime = self.Slime_Sheet.subsurface(self.Slime_Sheet.get_clip())

                    self.screen.blit(draw_Slime, pygame.Rect(x, y, 800, 600))
                    pygame.display.update()

                    if self.slimeF_counter == 240:
                        self.slimeF_counter = 0
                    else:
                        self.slimeF_counter += 1

                    pygame.display.update()

                   
        if direction == "U":
            self.slimeF_x = 160
            if self.slimeF_x < 200:
                self.Slime_Sheet.set_clip(pygame.Rect(self.slimeF_x, 0, 40, 40))
                draw_Slime = self.Slime_Sheet.subsurface(self.Slime_Sheet.get_clip())
                self.screen.blit(draw_Slime, pygame.Rect(x, y, 800, 600))
                self.slimeF_counter += 1

                pygame.display.update()

                self.slimeF_x += 40

                if self.slimeF_x == 200 and self.slimeF_counter >= 120 and self.slimeF_counter <= 240:
                    self.Slime_Sheet.set_clip(pygame.Rect(self.slimeF_x, 0, 40, 40))
                    draw_Slime = self.Slime_Sheet.subsurface(self.Slime_Sheet.get_clip())
                    self.screen.blit(draw_Slime, pygame.Rect(x, y, 800, 600))
                    if self.slimeF_counter == 240:
                        self.slimeF_counter = 0
                    else:
                        self.slimeF_counter += 1

                    pygame.display.update()

        if direction == "R":
            self.slimeF_x = 240
            if self.slimeF_x < 280:
                self.Slime_Sheet.set_clip(pygame.Rect(self.slimeF_x, 0, 40, 40))
                draw_Slime = self.Slime_Sheet.subsurface(self.Slime_Sheet.get_clip())
                self.screen.blit(draw_Slime, pygame.Rect(x, y, 800, 600))
                self.slimeF_counter += 1

                pygame.display.update()

                self.slimeF_x += 40

                if self.slimeF_x == 280 and self.slimeF_counter >= 120 and self.slimeF_counter <= 240:
                    self.Slime_Sheet.set_clip(pygame.Rect(self.slimeF_x, 0, 40, 40))
                    draw_Slime = self.Slime_Sheet.subsurface(self.Slime_Sheet.get_clip())
                    self.screen.blit(draw_Slime, pygame.Rect(x, y, 800, 600))
                    if self.slimeF_counter == 240:
                        self.slimeF_counter = 0
                    else:
                        self.slimeF_counter += 1

                    pygame.display.update()


        if direction == "D":
            self.slimeF_x = 0
            if self.slimeF_x < 40:
                self.Slime_Sheet.set_clip(pygame.Rect(self.slimeF_x, 0, 40, 40))
                draw_Slime = self.Slime_Sheet.subsurface(self.Slime_Sheet.get_clip())
                self.screen.blit(draw_Slime, pygame.Rect(x, y, 800, 600))
                self.slimeF_counter += 1

                pygame.display.update()

                self.slimeF_x += 40

                if self.slimeF_x == 40 and self.slimeF_counter >= 120 and self.slimeF_counter <= 240:
                    self.Slime_Sheet.set_clip(pygame.Rect(self.slimeF_x, 0, 40, 40))
                    draw_Slime = self.Slime_Sheet.subsurface(self.Slime_Sheet.get_clip())
                    self.screen.blit(draw_Slime, pygame.Rect(x, y, 800, 600))
                    if self.slimeF_counter == 240:
                        self.slimeF_counter = 0
                    else:
                        self.slimeF_counter += 1

                    pygame.display.update()      

    def get_rect(self):
        return self.rect