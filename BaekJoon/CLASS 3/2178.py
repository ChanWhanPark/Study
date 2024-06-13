## 2178. 미로 탐색 (2024.6.13) | S1
from collections import deque

N, M = map(int, input().split())

def BFS(x, y):
  dx = [-1, 1, 0, 0]
  dy = [0, 0, 1, -1]
  
  queue = deque()
  queue.append([x, y])
  
  while queue:
    a, b = queue.popleft()
    for i in range(4):
      nx = a + dx[i]
      ny = b + dy[i]
      
      if nx < 0 or nx >= N or ny < 0 or ny >= M:
        continue
      if graph[nx][ny] == 0:
        continue
      if graph[nx][ny] == 1:
        graph[nx][ny] = graph[a][b] + 1
        queue.append([nx, ny])

graph = [];
for _ in range(N):
  graph.append(list(map(int, input())))


BFS(0, 0)
print(graph[N-1][M-1])