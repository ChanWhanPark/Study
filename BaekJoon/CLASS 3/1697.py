## 1697. 숨바꼭질 (2024.6.10) | S1
from collections import deque

def bfs():
  q = deque()
  q.append(N)
  while q:
    x = q.popleft()
    if x == K: # x가 원하는 위치에 도착한 경우
      print(arr[x])
      break
    for nx in (x - 1, x + 1, x * 2) : # 세 가지 경우
      if 0 <= nx <= 100000 and not arr[nx]:
        arr[nx] = arr[x] + 1
        q.append(nx)

N, K = map(int, input().split());

arr = [0] * 100001
bfs()
