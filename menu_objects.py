import pygame
import os
from map_editor import *
import case_handler as ch

class Title_Menu(pygame.font.Font):

    def __init__(self, screen, case):

        self.screen = screen

        self.case = case

        self.screen_x = 800
        self.screen_y = 600

        self.screen = pygame.display.set_mode((self.screen_x, self.screen_y))
        self.screen.fill((255,255,255))

        self.Title_Title_Font = pygame.font.Font("menu_font.ttf", 60)
        self.Title_Menu_Font = pygame.font.Font("menu_font.ttf", 30)

        self.red = (255, 0 , 0)
        self.blue = (0, 0, 255)
        self.black = (0, 0, 0)



        self.Title_Title = self.Title_Title_Font.render("menu test", 1, self.black)

        self.Title_Menu_Item_x = 100
        self.Title_Menu_Item_y = 250
        self.Title_Menu_Item_y_spacer = 35

        self.Title_Menu_Items = {
        "Continue": (self.Title_Menu_Item_x, self.Title_Menu_Item_y), 
        "New Game": (self.Title_Menu_Item_x, self.Title_Menu_Item_y + self.Title_Menu_Item_y_spacer), 
        "Map Editor": (self.Title_Menu_Item_x, self.Title_Menu_Item_y + 2* self.Title_Menu_Item_y_spacer),
        "Quit": (self.Title_Menu_Item_x, self.Title_Menu_Item_y + 3* self.Title_Menu_Item_y_spacer)
        }

    def draw(self):
        self.screen.blit(self.Title_Title, (100,100))
        #self.screen.fill((255,255,255))
        for Title_Menu_Item in self.Title_Menu_Items:
            self.Title_Menu = self.Title_Menu_Font.render(Title_Menu_Item, 1, self.red)
            if self.Title_Menu.get_rect(topleft = (self.Title_Menu_Items[Title_Menu_Item])).collidepoint(pygame.mouse.get_pos()):
                self.Title_Menu = self.Title_Menu_Font.render(Title_Menu_Item, 1, self.blue)
                if pygame.mouse.get_pressed()[0]:
                    if Title_Menu_Item == "Quit":
                        pygame.quit()
                    elif Title_Menu_Item == "Continue":
                        print("Continue")
                    elif Title_Menu_Item == "New Game":
                        print("New Game")
                    elif Title_Menu_Item == "Map Editor":
                        self.case.update(ch.updateDict(self.case, 'Map Editor'))
                    elif Title_Menu_Item == "Options":
                        options_menu()

            self.screen.blit(self.Title_Menu, self.Title_Menu_Items[Title_Menu_Item])


    def get_rect(self):
        return self.rect



class Game_Menu(pygame.font.Font):

    def __init__(self, screen, case):

        self.screen = screen

        self.Game_Menu_Font = pygame.font.Font("menu_font.ttf", 15)

        self.white = (255, 255, 255)
        self.blue = (0, 0, 255)
        self.black = (0, 0, 0)

        self.Game_Menu_Item_x = 40
        self.Game_Menu_Item_y = 40
        self.Game_Menu_Item_y_spacer = 20

        self.Game_Menu_Items = {
        " Options": (self.Game_Menu_Item_x, self.Game_Menu_Item_y),
        " Quit": (self.Game_Menu_Item_x, self.Game_Menu_Item_y + self.Game_Menu_Item_y_spacer)
        }

    def get_rect(self):
        return self.rect

    def draw(self):
        self.Game_Menu_back_width = 160
        self.Game_Menu_back_height = 75
        pygame.draw.rect(self.screen, self.white, (20, 20, self.Game_Menu_back_width, self.Game_Menu_back_height))
        self.Game_Menu_back = pygame.draw.rect(self.screen, self.blue, (30, 30, self.Game_Menu_back_width - 20, self.Game_Menu_back_height - 20))

        for Game_Menu_Item in self.Game_Menu_Items:
            self.Game_Menu = self.Game_Menu_Font.render(Game_Menu_Item, 1, self.white)
            if self.Game_Menu.get_rect(topleft = (self.Game_Menu_Items[Game_Menu_Item])).collidepoint(pygame.mouse.get_pos()):
                self.Game_Menu = self.Game_Menu_Font.render("▶" + Game_Menu_Item[1:], 1, self.white)
                if pygame.mouse.get_pressed()[0]:
                    if Game_Menu_Item == " Quit":
                        pygame.quit()
                    elif Game_Menu_Item == " Options":
                        print("Options")
                        
            self.screen.blit(self.Game_Menu, self.Game_Menu_Items[Game_Menu_Item])

