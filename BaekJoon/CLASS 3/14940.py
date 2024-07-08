## 14940. 쉬운 최단거리 (2024.7.8) | S1
from collections import deque

N, M = map(int, input().split())
graph = []
for _ in range(N):
  graph.append(list(map(int, input().split())))

result = [0 * M for _ in range(N)]
visited = [[-1] * M for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def BFS(x, y):
  queue = deque()
  queue.append((x, y))
  visited[x][y] = 0
  
  while queue:
    nx, ny = queue.popleft();
    for i in range(4):
      new_x = nx + dx[i]
      new_y = ny + dy[i]
      
      if 0 <= new_x < N and 0 <= new_y < M and visited[new_x][new_y] == -1:
        if graph[new_x][new_y] == 0:
          visited[new_x][new_y] = 0
        elif graph[new_x][new_y] == 1:
          visited[new_x][new_y] = visited[nx][ny] + 1
          queue.append((new_x, new_y))

for i in range(N):
  for j in range(M):
    if graph[i][j] == 2:
      BFS(i, j)
      
      
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            print(0, end=' ')
        else:
            print(visited[i][j], end=' ')
    print()