import pygame

pygame.init()

screen_x = 800
screen_y = 600

screen = pygame.display.set_mode((screen_x, screen_y))
screen.fill((255,255,255))
pygame.display.set_caption("Menu test")

pygame.display.flip()

Title_Title_Font = pygame.font.SysFont("Arial", 60)
Title_Menu_Font = pygame.font.SysFont("Arial", 30)

grey = (100, 100, 100)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

Title_Title = Title_Title_Font.render("menu test", 1, (0, 0, 0))

Title_Menu_items = {"Continue": (100, 250), "New Game": (100, 290), "Level Editor": (100, 330), "Quit": (100, 370)}

TitleMenu = True
running = True

while running:

    if TitleMenu:
        screen.blit(Title_Title, (100, 100))

        for item in Title_Menu_items:
            Title_Menu = Title_Menu_Font.render(item, 1, red)
            if Title_Menu.get_rect(topleft = (Title_Menu_items[item])).collidepoint(pygame.mouse.get_pos()):
                print("test")
                Title_Menu = Title_Menu_Font.render(item, 1, blue)
            screen.blit(Title_Menu, Title_Menu_items[item])
        

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
            running = False


    pygame.display.flip()

    pygame.display.update()

pygame.quit()