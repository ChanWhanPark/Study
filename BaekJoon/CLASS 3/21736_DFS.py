## 21736. 헌내기는 친구가 필요해 (2024.5.31) | S2
import sys
sys.setrecursionlimit(10**6) # RecursionError
input = sys.stdin.readline # 시간 초과

N, M = map(int, input().split())
graph = list(input() for _ in range(N))
visited = [[False] * M for _ in range(N)]

cnt = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
  global cnt
  visited[x][y] = True
  if graph[x][y] == 'P':
    cnt += 1
  
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
      if graph[nx][ny] != 'X':
        dfs(nx, ny)

for i in range(N):
  for j in range(M):
    if graph[i][j] == "I":
      dfs(i, j)
      
if cnt == 0:
  print("TT")
else:
  print(cnt)