## 2667. 단지번호 붙이기 (2024.6.23) | S1
from collections import deque


# 그래프의 탐색 시작점을 모르기 때문에 전체를 돌면서 1인 지점에서 탐색을 시작함.

# 탐색 중 1인 부분은 0으로 바꿔 다시 방문하지 않도록 하고
# 한 번의 BFS가 끝나게 되면 더 이상 확장이 불가능 하므로 마을 하나가 생김.

# 이 마을안의 1의 개수들을 출력하면 되므로 다음 코드와 같이 result를 반환함.

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
  queue = deque()
  queue.append([x, y])
  graph[x][y] = 0
  count = 1
  
  while queue:
    x, y = queue.popleft();
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      
      if nx < 0 or nx >= N or ny < 0 or ny >= N:
        continue
      if graph[nx][ny] == 1:
        graph[nx][ny] = 0
        queue.append([nx, ny])
        count += 1
        
      
  result.append(count)
        
      

N = int(input())

graph = []
for _ in range(N):
  graph.append(list(map(int, input())))
  
result = []
visited = list([False] * N for _ in range(N))

for i in range(N):
  for j in range(N):
    if graph[i][j] == 1:
      bfs(i, j)
      
result.sort()
print(len(result))

for i in range(len(result)):
  print(result[i])