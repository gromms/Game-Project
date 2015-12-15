import pygame
import os
from pygame.locals import *

class Mob_Slime(pygame.sprite.Sprite):

    def __init__(self, screen):

        self.screen_x = 800
        self.screen_y = 600

        self.screen = screen

        self.Slime_dir = "./Imgs/slime/"
        self.S_d = (40, 40)
        
        self.direction = "left" 

        if self.direction == "left":
            self.Slime_Left_1 = pygame.image.load("./Imgs/slime/s_1L_1.png")
            self.Slime_Left_2 = pygame.image.load("./Imgs/slime/s_1L_2.png")

    def loadImgs(self):
        self.Slime_Sprites = []

        for slime_img in os.listdir(self.Slime_dir):
            if slime_img.endswith(".png"):
                imageRaw = pygame.image.load(slime_img).convert()
                self.image = pygame.transform.scale(imageRaw, (self.S_d))
                self.Slime_Sprite.append(self.image)

        print(self.Slime_Sprites)

    def draw(self):
        f = 0
        if self.direction == "left":
            if f == 0:
                self.screen.blit((self.Slime_Left_1), self.Slime_Left_1.get_rect())
                pygame.display.update()
                f = 1
            if f == 1:
                self.screen.blit((self.Slime_Left_1), self.Slime_Left_2.get_rect())
                pygame.display.update()
                f = 0



    def get_rect(self):
        return self.rect


