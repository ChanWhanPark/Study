## 16928. 뱀과 사다리 게임 (2024.7.28) | G5
from collections import deque

N, M = map(int, input().split())

board = [0] * 101
visited = [False] * 101

# 사다리
ladders = {}
for _ in range(N):
  x, y = map(int, input().split())
  ladders[x] = y
  
# 뱀
snakes = {}
for _ in range(M):
  u, v = map(int, input().split())
  snakes[u] = v
  
def BFS(start):
  q = deque()
  q.append(start)
  
  visited[start] = True
  
  while q:
    current = q.popleft()
    
    for i in range(1, 7): # 주사위 1~6
      next = current + i 
      
      if 0 < next <= 100 and not visited[next]:
        if next in ladders:
          next = ladders[next]
          
        if next in snakes:
          next = snakes[next]
          
        if not visited[next]:
          q.append(next)
          visited[next] = True
          board[next] = board[current] + 1
          
BFS(1)
print(board[100])