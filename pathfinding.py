def findLoc(mapList, a):
	for y in range(0, len(mapList)):
		for x in range(0, len(mapList[y][0])):
			if mapList[y][x] == a:
				return x, y
	return None

def createMapList(fileName):
	with open(fileName) as f:
		mapList = f.readlines()
		for i in range(0, len(mapList)):
			mapList[i] = mapList[i].strip().split()
	return mapList

def findAdj(point):
	adj1 = point[0] - 1, point[1]
	adj2 = point[0] + 1, point[1]
	adj3 = point[0], point[1] - 1
	adj4 = point[0], point[1] + 1

	adjList = [adj1, adj2, adj3, adj4]

	return adjList

def findPath(mapList, start, finish):
	queue = [finish]
	checked = set()
	lastPoint = {}
	pathFound = False
	while len(queue) > 0:
		i = queue.pop(0)
		checked.add(i)
		if i[0] == start[0] and i[1] == start[1]:
			break
		for adj in findAdj(i):
			if mapList[adj[0]][adj[1]] != 'X' and adj not in checked:
				queue.append(adj)
				if adj not in lastPoint:
					lastPoint[adj] = i

	path = [start]
	currPoint = start
	while path[len(path) - 1] != finish:
		currPoint = lastPoint[currPoint]
		path.append(currPoint)
	return path

def pathfinding(mapList, start, finish):
	if isinstance(start, str):
		start = findLoc(mapList, start)
	elif isinstance(finish, str):
		finish = findLoc(mapList, finish)
	return findPath(mapList, start, finish)