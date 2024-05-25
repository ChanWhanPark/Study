## 11279. 최대 힙 (2024.5.25) | S2
import sys
import heapq
input = sys.stdin.readline

N = int(input())

heap = []

for _ in range(N):
  x = int(input())
  
  if x == 0:
    if len(heap):
      value = (heapq.heappop(heap))
      print(value[1])
    else:
      print(0)
      
  else:
    heapq.heappush(heap, [-x, x])