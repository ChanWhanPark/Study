## 10026. 적록색약 (2024.7.28) | G5
import sys

sys.setrecursionlimit(10000)

N = int(input())

array = [[] * N for _ in range(N)]
for i in range(N):
    array[i] = list(sys.stdin.readline().strip())

cnt = 0
visited = [[False] * N for _ in range(N)]

def bfs(a,b,eyes,color):
  dx = [0, 0, -1, 1]
  dy = [-1, 1, 0, 0]

  for i in range(4):
    x = a + dx[i]
    y = b + dy[i]
    if x < 0 or x >= N or y < 0 or y >= N or visited[x][y]:
      continue

    if(eyes == 'b'):
      if((color != 'B') and array[x][y] != 'B'):
        visited[x][y] = True
        bfs(x, y, eyes, color)
      elif(color == 'B' and array[x][y] =='B'):
        visited[x][y] = True
        bfs(x, y, eyes, color)
      else:
        continue


    else:
      if color == array[x][y]:
        visited[x][y] = True
        bfs(x,y,eyes,color)

  return

# 적록색약이 아닌경우
for i in range(N):
  for j in range(N):
    if not visited[i][j]:
      bfs(i,j,'a',array[i][j])
      cnt += 1

print(cnt,end=' ')

# 적록색약인 경우
visited= [[False]*N for _ in range(N)]
cnt = 0
for i in range(N):
  for j in range(N):
    if not visited[i][j] :
      bfs(i,j,'b',array[i][j])
      cnt += 1
print(cnt)