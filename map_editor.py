import pygame
import os
import case_handler as ch
import maps

class Map_Editor():

	def __init__(self, screen, screen_x, screen_y):
		self.screen = screen

		self.screen_x = screen_x
		self.screen_y = screen_y

		#pygame.display.set_caption('Map Editor')
	
		self.tile_size = 40

		self.handler = maps.Map_Handler(self.tile_size)

	def main(self):
		self.sprites = maps.Map_Handler.loadImgs(self)

		print(self.sprites)

		rectPos = []
		mapList = []
		color_dict = {}

		elements = ['X', 'S', 'O', 'G']
		#self.images = {'G' : self.image}
		num = 0

		colors = [['red', (255, 0, 0)], ['green', (0, 255, 0)], ['blue', (0, 0, 255)], ['black', (0, 0, 0, 255)]]

		for color in colors:
			color_dict[color[0]] = color[1]

		mapName = input('Map name: ')
		mapName += '.txt'
		print(mapName)
		mapsFound = []
		for m in os.listdir('./Maps/'):
			mapsFound.append(m)

		if not mapName in mapsFound:
			#print('Created')
			mapList = self.handler.createMap(self.screen_x, self.screen_y)
			print('Created', mapList)
		else:
			#print('Found')
			mapList, rectPos = self.handler.loadMap(mapName)
			print('Found',mapList)
			#print(rectPos)
		pygame.display.flip()

		while True:
			self.screen.fill((255, 255, 255))
			mouse_posx, mouse_posy = pygame.mouse.get_pos()
			mouse_posx = mouse_posx // self.tile_size * self.tile_size
			mouse_posy = mouse_posy // self.tile_size * self.tile_size

			tile_center_x = mouse_posx + self.tile_size // 2
			tile_center_y = mouse_posy + self.tile_size // 2

			tile_pos_x = mouse_posx // self.tile_size
			tile_pos_y = mouse_posy // self.tile_size
			
			tile = pygame.Rect(mouse_posx, mouse_posy, self.tile_size, self.tile_size)

			event = pygame.event.poll()
			
			for rects in rectPos:
				if rects[2] == 'X':
					pygame.draw.rect(self.screen, color_dict['black'], rects[0])
				elif rects[2] == 'S':
					pygame.draw.rect(self.screen, color_dict['red'], rects[0])
				elif rects[2] == 'O':
					pygame.draw.rect(self.screen, color_dict['green'], rects[0])
				elif rects[2] == 'G':
					self.screen.blit(self.sprites['G'], rects[0])

			if event.type == pygame.QUIT:
				self.screen.fill((255,255,255))
				return True

			elif event.type == pygame.MOUSEBUTTONDOWN:
				if pygame.mouse.get_pressed()[0] or pygame.mouse.get_pressed()[1]:
					element = elements[num]
					rect = pygame.Rect(mouse_posx, mouse_posy, self.tile_size, self.tile_size)
					inList = False
					for i in range(0, len(rectPos)):
						if (tile_pos_x, tile_pos_y) in rectPos[i]:
							rectPos[i] = rect, (tile_pos_x, tile_pos_y), element 
							inList = True
							break
					if not inList:
						rectPos.append([rect, (tile_pos_x, tile_pos_y), element])

				elif pygame.mouse.get_pressed()[2]:
					for i in range(0, len(rectPos)):
						if rectPos[i][1] == (tile_pos_x, tile_pos_y):
							rectPos.remove(rectPos[i])
							break
			
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_s:
					self.handler.saveMap(mapName, mapList, rectPos)
				elif event.key == pygame.K_l:
					mapList, rectPos = self.handler.loadMap(mapName)
				elif event.key == pygame.K_LEFT:
					if num > 0:
						num -= 1
				elif event.key == pygame.K_RIGHT:
					if num < len(elements) - 1:
						num += 1
				elif event.key == pygame.K_ESCAPE:
					self.screen.fill((255,255,255))
					return 1
			
			pygame.display.update()