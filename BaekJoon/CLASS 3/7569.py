## 7569. 토마토 (2024.7.22) | G5
from collections import deque

M, N, H = map(int, input().split())
tomato = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
queue = deque()

for i in range(H):
  for j in range(N):
    for k in range(M):
      if tomato[i][j][k] == 1:
        queue.append((i, j, k))
        
while queue:
  z, x, y = queue.popleft()
  for i in range(6):
    nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]
    if 0 <= nx < N and 0 <= ny < M and 0 <= nz < H:
      if tomato[nz][nx][ny] == 0:
        tomato[nz][nx][ny] = tomato[z][x][y] + 1
        queue.append((nz, nx, ny))
        
cant_complete = False
day = 0

print(tomato)
for i in range(H):
  for j in range(N):
    for k in range(M):
      if tomato[i][j][k] == 0:
        cant_complete = True
      day = max(day, tomato[i][j][k])
      
if cant_complete:
  print(-1)
else:
  print(day - 1)