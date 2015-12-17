import pygame
import os
import case_handler as ch
import maps
import monster_objects as mobs
import character_objects as chars
import pathfinding as pathf

class Game_Core():
	def __init__(self, screen, screen_x, screen_y):
		self.screen = screen

		self.screen_x = screen_x
		self.screen_y = screen_y

		#pygame.display.set_caption('')
	
		self.tile_size = 40

		self.handler = maps.Map_Handler(self.tile_size)
		self.slime = mobs.Mob_Slime(screen)
		self.character = chars.Main_Char(screen)

	def main(self):
		#print('GAME!')
		self.sprites = maps.Map_Handler.loadImgs(self)

		clock = pygame.time.Clock()

		mapList, rectPos = self.handler.loadMap('testmap.txt')
		#print(mapList)
		#print(rectPos)

		pygame.display.flip()

		playerPosX = 1
		playerPosY = 1
		playerDir = 'D'

		slimePosX = 10
		slimePosY = 10
		slimeDir = 'D'

		color_dict = {}
		colors = [['red', (255, 0, 0)], ['green', (0, 255, 0)], ['blue', (0, 0, 255)], ['black', (0, 0, 0, 255)]]

		for color in colors:
			color_dict[color[0]] = color[1]

		while True:
			limit = clock.tick(150)
			#print(limit)
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
			#print(slimePosX, slimePosY)
			self.slime.draw(slimeDir, slimePosX, slimePosY)
			self.character.draw(playerDir, playerPosX, playerPosY)

			if event.type == pygame.QUIT:
				self.screen.fill((255,255,255))
				return True

			elif event.type == pygame.MOUSEBUTTONDOWN:
				if pygame.mouse.get_pressed()[0]:
					#print('pressed', tile_pos_x, tile_pos_y)
					if mapList[tile_pos_y][tile_pos_x] != 'X':
						#for i in mapList:
						#	print(i)
						path = pathf.pathfinding(mapList, (playerPosX, playerPosY), (tile_pos_x, tile_pos_y))
<<<<<<< HEAD

=======
						#print(len(path), path)
						'''for step in range(1, len(path)):
							if step < len(path):
								print('Current pos:', slimePosX, slimePosY, ';', 'Next step:',path[step])
								if slimePosX > path[step][0]:
									slimeDir = 'L'
									slimePosX -= 1
									print(slimeDir)
								elif slimePosX < path[step][0]:
									slimeDir = 'R'
									slimePosX += 1
									print(slimeDir)
								elif slimePosY > path[step][1]:
									slimeDir = 'U'
									slimePosY -= 1
									print(slimeDir)
								elif slimePosY < path[step][1]:
									slimeDir = 'D'
									slimePosY += 1
									print(slimeDir)'''
>>>>>>> 81af2e7d818a22be0b40060baae8c8fb44c9e812
						for step in range(1, len(path)):
							if step < len(path):
								#print('Current pos:', playerPosX, playerPosY, ';', 'Next step:',path[step])
								if playerPosX > path[step][0]:
									playerDir = 'L'
									playerPosX -= 1
<<<<<<< HEAD
									#print(playerDir)
								elif playerPosX < path[step][0]:
									playerDir = 'R'
									playerPosX += 1
									#print(playerDir)
								elif playerPosY > path[step][1]:
									playerDir = 'U'
									playerPosY -= 1
									#print(playerDir)
								elif playerPosY < path[step][1]:
									playerDir = 'D'
									playerPosY += 1
									#print(playerDir)										
									
=======
									print(playerDir)
								elif playerPosX < path[step][0]:
									playerDir = 'R'
									playerPosX += 1
									print(playerDir)
								elif playerPosY > path[step][1]:
									playerDir = 'U'
									playerPosY -= 1
									print(playerDir)
								elif playerPosY < path[step][1]:
									playerDir = 'D'
									playerPosY += 1
									print(playerDir)										

							#self.slime.draw(slimeDir, slimePosX, slimePosY)
>>>>>>> 81af2e7d818a22be0b40060baae8c8fb44c9e812
							self.character.draw(playerDir, playerPosX, playerPosY)
							pygame.display.update()
							pygame.time.delay(20)

			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					self.screen.fill((255, 255, 255))
					return 1

			pygame.display.update()