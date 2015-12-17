import pygame
import os
from pygame.locals import *

class Main_Char(pygame.sprite.Sprite):

    def __init__(self, screen):

        self.screen = screen

        self.screen_x = 800
        self.screen_y = 600

        self.Char_Sheet = pygame.image.load("./Imgs/char/char_spritesheet.png").convert_alpha()

        self.charF_counter = 0

        self.charF_x = 0

        self.Char_speed = 3

    def get_rect():
        return self.rect

    def draw(self, direction, x, y):
        x = x*40
        y = y*40

        if direction == "L":
            self.charF_x = 160
            if self.charF_x < 200:
                self.Char_Sheet.set_clip(pygame.Rect(self.charF_x, 0, 40, 40))
                draw_Char = self.Char_Sheet.subsurface(self.Char_Sheet.get_clip())
                self.screen.blit(draw_Char, pygame.Rect(x, y, 800, 600))

                self.charF_counter += 1

                pygame.display.update()

                self.charF_x += 40

                if self.charF_x == 200 and self.charF_counter >= 120 and self.charF_counter <= 240:
                    self.Char_Sheet.set_clip(pygame.Rect(self.charF_x, 0, 40, 40))
                    draw_Char = self.Char_Sheet.subsurface(self.Char_Sheet.get_clip())
                    self.screen.blit(draw_Char, pygame.Rect(x, y, 800, 600))
                    pygame.display.update()

                    if self.charF_counter == 240:
                        self.charF_counter = 0
                    else:
                        self.charF_counter += 1

                    pygame.display.update()


        if direction == "D":
            self.charF_x = 0
            if self.charF_x < 40:
                self.Char_Sheet.set_clip(pygame.Rect(self.charF_x, 0, 40, 40))
                draw_Char = self.Char_Sheet.subsurface(self.Char_Sheet.get_clip())
                self.screen.blit(draw_Char, pygame.Rect(x, y, 800, 600))

                self.charF_counter += 1

                pygame.display.update()

                self.charF_x += 40

                if self.charF_x == 40 and self.charF_counter >= 120 and self.charF_counter <= 240:
                    self.Char_Sheet.set_clip(pygame.Rect(self.charF_x, 0, 40, 40))
                    draw_Char = self.Char_Sheet.subsurface(self.Char_Sheet.get_clip())
                    self.screen.blit(draw_Char, pygame.Rect(x, y, 800, 600))
                    pygame.display.update()

                    if self.charF_counter == 240:
                        self.charF_counter = 0
                    else:
                        self.charF_counter += 1

                    pygame.display.update()


        if direction == "U":
            self.charF_x = 80
            if self.charF_x < 120:
                self.Char_Sheet.set_clip(pygame.Rect(self.charF_x, 0, 40, 40))
                draw_Char = self.Char_Sheet.subsurface(self.Char_Sheet.get_clip())
                self.screen.blit(draw_Char, pygame.Rect(x, y, 800, 600))

                self.charF_counter += 1

                pygame.display.update()

                self.charF_x += 40

                if self.charF_x == 120 and self.charF_counter >= 120 and self.charF_counter <= 240:
                    self.Char_Sheet.set_clip(pygame.Rect(self.charF_x, 0, 40, 40))
                    draw_Char = self.Char_Sheet.subsurface(self.Char_Sheet.get_clip())
                    self.screen.blit(draw_Char, pygame.Rect(x, y, 800, 600))
                    pygame.display.update()

                    if self.charF_counter == 240:
                        self.charF_counter = 0
                    else:
                        self.charF_counter += 1

                    pygame.display.update()


        if direction == "R":
            self.charF_x = 240
            if self.charF_x < 280:
                self.Char_Sheet.set_clip(pygame.Rect(self.charF_x, 0, 40, 40))
                draw_Char = self.Char_Sheet.subsurface(self.Char_Sheet.get_clip())
                self.screen.blit(draw_Char, pygame.Rect(x, y, 800, 600))

                self.charF_counter += 1

                pygame.display.update()

                self.charF_x += 40

                if self.charF_x == 280 and self.charF_counter >= 120 and self.charF_counter <= 240:
                    self.Char_Sheet.set_clip(pygame.Rect(self.charF_x, 0, 40, 40))
                    draw_Char = self.Char_Sheet.subsurface(self.Char_Sheet.get_clip())
                    self.screen.blit(draw_Char, pygame.Rect(x, y, 800, 600))
                    pygame.display.update()

                    if self.charF_counter == 240:
                        self.charF_counter = 0
                    else:
                        self.charF_counter += 1

                    pygame.display.update()