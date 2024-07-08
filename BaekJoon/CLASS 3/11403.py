## 11403. 경로 찾기 (2024.7.8) | S1
### 각 정점마다 방문했는지의 여부를 result에 저장하고
### 간선으로 해당 정점이 연결되어 있다면 check에 1을 기록한다.
from collections import deque

G = []
N = int(input())
for _ in range(N):
  G.append(list(map(int, input().split())))
result = [[0] * N for _ in range(N)]

def BFS(x):
  queue = deque()
  queue.append(x)
  check = [0 for _ in range(N)]
  
  while queue:
    q = queue.popleft()
    
    for i in range(N):
      if check[i] == 0 and G[q][i] == 1:
        queue.append(i)
        check[i] = 1
        result[x][i] = 1

for i in range(N):
  BFS(i)
  
for i in result:
  print(*i)
