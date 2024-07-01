## 11286. 절댓값 힙 (2024.6.30) | S1
import heapq

N = int(input())
heap = []

for _ in range(N):
  num = int(input())
  if num != 0:
    heapq.heappush(heap, (abs(num), num))
  else:
    try:
      print(heapq.heappop(heap)[1])
    except:
      print(0)