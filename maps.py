import pygame
import os

class Map_Handler():

	def __init__(self, tile_size):
		self.tile_size = tile_size

	def loadImgs(self):
		self.sprites = {}

		for i in os.listdir('./Imgs/'):
			if len(str(i)) == 5 and os.path.isfile(os.path.join('./Imgs/', i)):
				print(i)
				imageRaw = pygame.image.load('./Imgs/' + i).convert()
				self.image = pygame.transform.scale(imageRaw, (self.tile_size, self.tile_size))
				self.sprites[i[0]] = self.image

		return self.sprites	

	def saveMap(self, mapName, mapList, rectPos):
		#mapName += '.txt'
		#print(mapName)
		f = open('./Maps/'+mapName, 'w')
		print('Saving:', mapList)
		for y in range(0, len(mapList)):
			for x in range(0, len(mapList[y])):
				default = False
				for i in range(0, len(rectPos)):
					if (x, y) == rectPos[i][1]:
						f.write(rectPos[i][2])
						default = True
						break
				if not default:
					f.write('_')
			f.write('\n')
		print('Map saved!')
		f.close()

	def loadMap(self, mapName):
		#mapName += '.txt'
		#print(mapName)

		f = open('./Maps/'+mapName, 'r')
		mapList = []
		while True:
			line = f.readline().split()
			#print(line)
			if not line:
				break
			mapList.append([])
			#print(mapList)
			#print(len(str(line[0])))
			for i in range(0, len(str(line[0]))):
				mapList[len(mapList) - 1].append(line[0][i])

		rectPos = []

		for i in range(0, len(mapList)):
			#print(mapList[i])
			for j in range(0, len(mapList[i])):
				if mapList[i][j] != '_':
					rect = pygame.Rect(j * self.tile_size, i * self.tile_size, self.tile_size, self.tile_size)
					rectPos.append([rect, (j * self.tile_size, i * self.tile_size), mapList[i][j]])
		#print('Loaded', mapName)
		#print(rectPos)
		f.close()
		return mapList, rectPos

	def createMap(self, screen_x, screen_y):
		
		mapList = []
		rectPos = []

		for i in range(0, self.screen_y // self.tile_size):
			mapList.append([])
			for j in range(0, self.screen_x // self.tile_size):
				mapList[i].append('_')

		print(mapList)
		return mapList


