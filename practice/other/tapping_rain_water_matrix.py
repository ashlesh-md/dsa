class Node:
	def __init__(self, height, x, y):
		self.height = height
		self.x = x
		self.y = y

class Compare:

	def __lt__(self, a, b):
		return a.height > b.height

def trapRainWater(heightMap):
	M = len(heightMap)
	N = len(heightMap[0])

	visited = [[False for _ in range(N)] for _ in range(M)]
	pq = []

	for i in range(M):
		for j in range(N):

			if i == 0 or j == 0 or i == M - 1 or j == N - 1:
				visited[i][j] = True
				t = Node(heightMap[i][j], i, j)
				pq.append(t)
	ans = 0
	max_height = float('-inf')
	while pq:
		front = pq.pop()
		max_height = max(max_height, front.height)
		curr_x = front.x
		curr_y = front.y

		for i in range(4):
			new_x = curr_x + dir[i][0]
			new_y = curr_y + dir[i][1]
			if new_x < 0 or new_y < 0 or new_x >= M or new_y >= N or visited[new_x][new_y]:
				continue
			height = heightMap[new_x][new_y]
			if height < max_height:
				ans += (max_height - height)
			temp = Node(height, new_x, new_y)
			pq.append(temp)
			visited[new_x][new_y] = True

	return ans


arr = [[1, 4, 3, 1, 3, 2], [3, 2, 1, 3, 2, 4], [2, 3, 3, 2, 3, 1]]
print(trapRainWater(arr))
