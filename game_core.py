import pygame
import os
import case_handler as ch
import maps
import monster_objects as mobs
import pathfinding as pathf

class Game_Core():
	def __init__(self, screen, screen_x, screen_y):
		self.screen = screen

		self.screen_x = screen_x
		self.screen_y = screen_y

		pygame.display.set_caption('Game')
	
		self.tile_size = 40

		self.handler = maps.Map_Handler(self.tile_size)
		self.slime = mobs.Mob_Slime(screen)

	def main(self):
		#print('GAME!')
		self.sprites = maps.Map_Handler.loadImgs(self)

		mapList, rectPos = self.handler.loadMap('testmap.txt')
		#print(mapList)
		#print(rectPos)

		pygame.display.flip()

		playerPosX = 2
		playerPosY = 2

		slimePosX = 10 * self.tile_size
		slimePosY = 10 * self.tile_size
		slimeDir = 'D'

		color_dict = {}
		colors = [['red', (255, 0, 0)], ['green', (0, 255, 0)], ['blue', (0, 0, 255)], ['black', (0, 0, 0, 255)]]

		for color in colors:
			color_dict[color[0]] = color[1]

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

			self.slime.draw(slimeDir, slimePosX, slimePosY)

			if event.type == pygame.QUIT:
				self.screen.fill((255,255,255))
				return True

			elif event.type == pygame.MOUSEBUTTONDOWN:
				if pygame.mouse.get_pressed()[0]:
					print('pressed', tile_pos_x, tile_pos_y)
					if mapList[tile_pos_y][tile_pos_x] != 'X':
						
						path = pathf.pathfinding(mapList, (slimePosX, slimePosY), (tile_pos_x, tile_pos_y))
						print(path)
						for step in range(0, len(path)):
							if step != len(path) - 1:
								if slimePosX < path[step][0]:
									slimeDir = 'L'
									slimePosX -= self.tile_size // 2
								elif slimePosX > path[step][0]:
									slimeDir = 'R'
									slimePosX += self.tile_size // 2
								elif slimePosY < path[step][1]:
									slimeDir = 'U'
									slimePosY -= self.tile_size // 2
								elif slimePosY > path[step][1]:
									slimeDir = 'D'
									slimePosY += self.tile_size // 2

								self.slime.draw(slimeDir, slimePosX, slimePosY)
								pygame.display.update()

								if slimeDir == 'L':
									slimePosX -= self.tile_size // 2
								elif slimeDir == 'R':
									slimePosY += self.tile_size // 2
								elif slimeDir == 'U':
									slimePosY -= self.tile_size // 2
								elif slimeDir == 'D':
									slimePosY += self.tile_size // 2

								self.slime.draw(slimeDir, slimePosX, slimePosY)
								pygame.display.update()

			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					sl.screen.fill((255, 255, 255))
					return 1

			pygame.display.update()