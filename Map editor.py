import pygame

pygame.init()

screen_x = 800
screen_y = 600
tile_size = 40

screen = pygame.display.set_mode((screen_x, screen_y))
screen.fill((255, 255, 255))
pygame.display.set_caption('Map Editor')

rectPos = []

black = (0, 0, 0, 255)

pygame.display.flip()

while True:
	screen.fill((255, 255, 255))
	mouse_posx, mouse_posy = pygame.mouse.get_pos()
	mouse_posx = mouse_posx // tile_size * tile_size
	mouse_posy = mouse_posy // tile_size * tile_size
	tile = pygame.Rect(mouse_posx, mouse_posy, tile_size, tile_size)
	#pygame.draw.rect(screen, (0, 0, 0), tile)

	event = pygame.event.poll()

	for rects in rectPos:
		pygame.draw.rect(screen, (0, 0, 0), rects)

	if event.type == pygame.QUIT:
		break
	elif event.type == pygame.MOUSEBUTTONDOWN:
		rectPos.append(pygame.Rect(mouse_posx, mouse_posy, tile_size, tile_size))

		
	elif event.type == pygame.KEYDOWN:
		open('map_name.txt', 'w').close()
		print('asd')
		#map_name = input('Map name: ')
		#map_name += '.txt'
		for y in range(0, int(screen_y / tile_size)):
			y1 = int(y * tile_size + int(tile_size/2))
			mapList = ''
			for x in range(0, int(screen_x / tile_size)):
				x1 = int(x * tile_size + int(tile_size/2))
				print(x1, y1, tuple(screen.get_at((x1, y1))))
				if tuple(screen.get_at((x1+1, y1+1))) == black:
					print(x, y, 'X')
					mapList += 'X'
				else:
					mapList += '_'
			mapList += '\n'
			with open('map_name.txt', 'a') as f:
				f.write(mapList)
	pygame.display.update()
	#print(tile)
	
pygame.quit()