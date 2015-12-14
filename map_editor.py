import pygame
import os

#pygame.init()

def mapEditor(screen_x, screen_y, screen):
	#screen_x
	#screen_y

	tile_size = 40

	#screen = pygame.display.set_mode((screen_x, screen_y))
	#screen.fill((255, 255, 255))
	pygame.display.set_caption('Map Editor')

	sprites = {}

	for i in os.listdir('./Imgs/'):
		imageRaw = pygame.image.load('./Imgs/' + i).convert()
		image = pygame.transform.scale(imageRaw, (tile_size, tile_size))
		sprites[i[0]] = image

	print(sprites)
	#print(image.get_rect())

	rectPos = []
	mapList = []
	color_dict = {}

	elements = ['X', 'S', 'O', 'G']
	images = {'G' : image}
	num = 0

	colors = [['red', (255, 0, 0)], ['green', (0, 255, 0)], ['blue', (0, 0, 255)], ['black', (0, 0, 0, 255)]]

	for color in colors:
		color_dict[color[0]] = color[1]

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

		event = pygame.event.poll()
		
		for rects in rectPos:
			if rects[2] == 'X':
				pygame.draw.rect(screen, color_dict['black'], rects[0])
			elif rects[2] == 'S':
				pygame.draw.rect(screen, color_dict['red'], rects[0])
			elif rects[2] == 'O':
				pygame.draw.rect(screen, color_dict['green'], rects[0])
			elif rects[2] == 'G':
				screen.blit(sprites['G'], rects[0])

		if event.type == pygame.QUIT:
			break

		elif event.type == pygame.MOUSEBUTTONDOWN:
			if pygame.mouse.get_pressed()[0] or pygame.mouse.get_pressed()[1]:
				element = elements[num]
				rect = pygame.Rect(mouse_posx, mouse_posy, tile_size, tile_size)
				inList = False
				for i in range(0, len(rectPos)):
					if (tile_pos_x, tile_pos_y) in rectPos[i]:
						rectPos[i] = rect, (tile_pos_x, tile_pos_y), element 
						inList = True
						break
				if not inList:
					rectPos.append([rect, (tile_pos_x, tile_pos_y), element])

				#mapList[tile_pos_y][tile_pos_x] = 'X'
				print(rectPos)
			elif pygame.mouse.get_pressed()[2]:
				for i in range(0, len(rectPos)):
					if rectPos[i][1] == (tile_pos_x, tile_pos_y):
						rectPos.remove(rectPos[i])
						break
				print(rectPos)
		
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_s:
				f = open('mapName.txt', 'w')
				for y in range(0, len(mapList)):
					for x in range(0, len(mapList[y])):
						default = False
						for i in range(0, len(rectPos)):
							#print(rectPos[i][1])
							if (x, y) == rectPos[i][1]:
								#rint('X')
								f.write(rectPos[i][2])
								default = True
								break
						if not default:
							f.write('_')
						#f.write(mapList[y][x])
					f.write('\n')
				print('Map saved!')
				f.close()
			#f = open('map_name.txt')
			#print(f.readlines())
			elif event.key == pygame.K_LEFT:
				if num > 0:
					num -= 1
					print(elements[num])
			elif event.key == pygame.K_RIGHT:
				if num < len(elements) - 1:
					num += 1
					print(elements[num])
			elif event.key == pygame.K_ESCAPE:
				return 1
		
		pygame.display.update()
		#print(tile)