## 2606. 바이러스 (2024.4.19) | S3
computer = int(input())
network = int(input())

graph = [[] * computer for _ in range(computer + 1)]

for i in range(network):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a) # 양방향 그래프 입력
  
visited = [False] * (computer + 1)
count = 0

def dfs(start):
  global count;
  visited[start] = True;
  
  for i in graph[start]:
    if visited[i] == False:
      dfs(i)
      count += 1;
      
      
dfs(1)
print(count)

