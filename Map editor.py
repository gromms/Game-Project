import pygame

pygame.init()

screen_x = 800
screen_y = 600
tile_size = 40

screen = pygame.display.set_mode((screen_x, screen_y))
screen.fill((255, 255, 255))
pygame.display.set_caption('Map Editor')

rectPos = []
mapList = []

black = (0, 0, 0, 255)

for i in range(0, screen_y // tile_size):
	mapList.append([])
	for j in range(0, screen_x // tile_size):
		mapList[i].append('_')
print(mapList)

pygame.display.flip()

while True:
	screen.fill((255, 255, 255))
	mouse_posx, mouse_posy = pygame.mouse.get_pos()
	mouse_posx = mouse_posx // tile_size * tile_size
	mouse_posy = mouse_posy // tile_size * tile_size

	tile_center_x = mouse_posx + tile_size // 2
	tile_center_y = mouse_posy + tile_size // 2

	tile_pos_x = mouse_posx // tile_size
	tile_pos_y = mouse_posy // tile_size
	
	tile = pygame.Rect(mouse_posx, mouse_posy, tile_size, tile_size)
	#pygame.draw.rect(screen, (0, 0, 0), tile)

	event = pygame.event.poll()

	for rects in rectPos:
		pygame.draw.rect(screen, (0, 0, 0), rects)

	if event.type == pygame.QUIT:
		break
	elif event.type == pygame.MOUSEBUTTONDOWN:
		if pygame.mouse.get_pressed()[0]:
			rect = pygame.Rect(mouse_posx, mouse_posy, tile_size, tile_size)
			rectPos.append(rect)
			mapList[tile_pos_y][tile_pos_x] = 'X'
			print(mapList)

	elif event.type == pygame.KEYDOWN:

		f = open('map_name.txt', 'w')
		for y in range(0, len(mapList)):
			for x in range(0, len(mapList[y])):
				f.write(mapList[y][x])
			f.write('\n')
		print('Map saved!')
			
	pygame.display.update()
	#print(tile)
	
pygame.quit()