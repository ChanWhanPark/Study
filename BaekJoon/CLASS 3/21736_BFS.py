from collections import deque

N, M = map(int, input().split())
graph = list(input() for _ in range(N))
visited = [[False] * M for _ in range(N)]

cnt = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
  global cnt;
  queue = deque([(x, y)])
  visited[x][y] = True
  
  while (queue):
    a, b = queue.popleft()
    
    for i in range(4):
      nx = dx[i] + a
      ny = dy[i] + b
      
      if 0 <= nx < N and 0 <= ny < M:
        if graph[nx][ny] != 'X' and not visited[nx][ny]:
          queue.append([nx, ny])
          visited[nx][ny] = True
          
          if graph[nx][ny] == 'P':
            cnt += 1

for i in range(N):
  for j in range(M):
    if graph[i][j] == "I":
      bfs(i, j)
      
if cnt > 0:
  print(cnt)
else:
  print('TT')