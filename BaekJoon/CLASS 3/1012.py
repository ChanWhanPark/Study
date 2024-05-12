## 1012. 유기농 배추 (2024.5.12) | S2
# BFS

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

T = int(input())

def BFS(x, y):
  queue = [(x, y)]
  graph[x][y] = 0 # 방문처리
  
  while queue:
    x_, y_ = queue.pop(0)
    
    for i in range(4):
      nx = x_ + dx[i]
      ny = y_ + dy[i]
      
      if nx < 0 or nx >= M or ny < 0 or ny >= N:
        continue
      
      if graph[nx][ny] == 1:
        queue.append((nx, ny))
        graph[nx][ny] = 0
  

for _ in range(T):
  M, N, K = map(int, input().split())
  graph = [[0] * N for _ in range(M)]
  cnt = 0
  
  for i in range(K):
    a, b = map(int, input().split())
    graph[a][b] = 1
    
  for x in range(M):
    for y in range(N):
      if graph[x][y] == 1:
        BFS(x, y)
        cnt += 1
        
  print(cnt)