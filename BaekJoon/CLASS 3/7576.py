## 7576. 토마토 (2024.8.4) | G5
from collections import deque

M, N = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
queue = deque()

for i in range(N):
  for j in range(M):
    if tomato[i][j] == 1:
      queue.append((i, j))
      
while queue:
  x, y = queue.popleft()
  for i in range(4):
    nx, ny = x + dx[i], y + dy[i]
    if 0 <= nx < N and 0 <= ny < M:
      if tomato[nx][ny] == 0:
        tomato[nx][ny] = tomato[x][y] + 1
        queue.append((nx, ny))
        
cant_complete = False
day = 0

for i in range(N):
  for j in range(M):
    if tomato[i][j] == 0:
      cant_complete = True
    day = max(day, tomato[i][j])
    
if cant_complete:
  print(-1)
else:
  print(day - 1)