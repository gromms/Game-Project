import pygame
import os
from pygame.locals import *

class Mob_Slime(pygame.sprite.Sprite):

    def __init__(self, screen):

        self.screen = screen

        self.Slime_Sheet = pygame.image.load("./Imgs/slime/slime_spritesheet.png").convert_alpha()

        self.slimeF_counter = 0

        self.slimeF_x = 0

    def draw(self, direction):

        if direction == "L":
            self.slimeF_x = 80
            if self.slimeF_x < 120:
                self.Slime_Sheet.set_clip(pygame.Rect(self.slimeF_x, 0, 40, 40))
                draw_Slime = self.Slime_Sheet.subsurface(self.Slime_Sheet.get_clip())
                self.screen.blit(draw_Slime, pygame.Rect(100, 100, 800, 600))
                self.slimeF_counter += 1

                pygame.display.update()

                self.slimeF_x += 40

                if self.slimeF_x == 120 and self.slimeF_counter >= 120 and self.slimeF_counter <= 240:
                    self.Slime_Sheet.set_clip(pygame.Rect(self.slimeF_x, 0, 40, 40))
                    draw_Slime = self.Slime_Sheet.subsurface(self.Slime_Sheet.get_clip())
                    self.screen.blit(draw_Slime, pygame.Rect(100, 100, 800, 600))
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
                self.screen.blit(draw_Slime, pygame.Rect(100, 100, 800, 600))
                self.slimeF_counter += 1

                pygame.display.update()

                self.slimeF_x += 40

                if self.slimeF_x == 200 and self.slimeF_counter >= 120 and self.slimeF_counter <= 240:
                    self.Slime_Sheet.set_clip(pygame.Rect(self.slimeF_x, 0, 40, 40))
                    draw_Slime = self.Slime_Sheet.subsurface(self.Slime_Sheet.get_clip())
                    self.screen.blit(draw_Slime, pygame.Rect(100, 100, 800, 600))
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
                self.screen.blit(draw_Slime, pygame.Rect(100, 100, 800, 600))
                self.slimeF_counter += 1

                pygame.display.update()

                self.slimeF_x += 40

                if self.slimeF_x == 280 and self.slimeF_counter >= 120 and self.slimeF_counter <= 240:
                    self.Slime_Sheet.set_clip(pygame.Rect(self.slimeF_x, 0, 40, 40))
                    draw_Slime = self.Slime_Sheet.subsurface(self.Slime_Sheet.get_clip())
                    self.screen.blit(draw_Slime, pygame.Rect(100, 100, 800, 600))
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
                self.screen.blit(draw_Slime, pygame.Rect(100, 100, 800, 600))
                self.slimeF_counter += 1

                pygame.display.update()

                self.slimeF_x += 40

                if self.slimeF_x == 40 and self.slimeF_counter >= 120 and self.slimeF_counter <= 240:
                    self.Slime_Sheet.set_clip(pygame.Rect(self.slimeF_x, 0, 40, 40))
                    draw_Slime = self.Slime_Sheet.subsurface(self.Slime_Sheet.get_clip())
                    self.screen.blit(draw_Slime, pygame.Rect(100, 100, 800, 600))
                    if self.slimeF_counter == 240:
                        self.slimeF_counter = 0
                    else:
                        self.slimeF_counter += 1

                    pygame.display.update()
        

    def get_rect(self):
        return self.rect




