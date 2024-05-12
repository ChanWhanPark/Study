## 1260. DFS와 BFS
def DFS(v):
  dfs_visited[v] = 1
  print(v, end = " ")
  
  for i in graph[v]:
    if dfs_visited[i] == 0:
      DFS(i)
      
def BFS(v):
  q = [(v)]; # queue
  bfs_visited[v] = 1
  while q:
    v = q.pop(0)
    print(v, end=" ")
    for i in graph[v]:
      if bfs_visited[i] == 0:
        q.append(i)
        bfs_visited[i] = 1

N, M, V = map(int, input().split())

graph = [[] * (N+1) for _ in range(N+1)]

for _ in range(M):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)
  
for i in graph:
  i.sort()
  
dfs_visited = [0] * (N+1)
bfs_visited = [0] * (N+1)

DFS(V)
print()
BFS(V)