## 11724. 연결 요소의 개수 (2024.5.25)
N, M = map(int, input().split())

graph = [[] * (N+1) for _ in range(N+1)]

answer = 0

for _ in range(M):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)
  
for i in graph:
  i.sort()
  
visited = [0] * (N+1)

def DFS(N):
  visited[N] = 1
  
  for i in graph[N]:
    if visited[i] == 0:
      DFS(i)

for i in range(1, N+1):
  if visited[i] == 0:
    DFS(i)
    answer += 1
    
print(answer)