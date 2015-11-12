import pygame

pygame.init()

screen_x = 800
screen_y = 600
tile_size = 40

screen = pygame.display.set_mode((screen_x, screen_y))
screen.fill((255, 255, 255))
pygame.display.set_caption('Map Editor')

pygame.display.flip()

while True:
	event = pygame.event.poll()
	if event.type == pygame.QUIT:
		break
	elif event.type == pygame.MOUSEBUTTONDOWN:
		print('asd')
	screen.fill((255, 255, 255))
	mouse_posx, mouse_posy = pygame.mouse.get_pos()
	mouse_posx = mouse_posx // tile_size * tile_size
	mouse_posy = mouse_posy // tile_size * tile_size
	tile = pygame.Rect(mouse_posx, mouse_posy, tile_size, tile_size)
	pygame.draw.rect(screen, (0, 0, 0), tile)
	pygame.display.update()
	#print(mouse_posx, mouse_posy)


pygame.quit()