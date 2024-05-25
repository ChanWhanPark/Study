## 1927. 최소 힙 (2024.5.19) | S2
import sys
import heapq
input = sys.stdin.readline
N = int(input())

heap = []

for _ in range(N):
  x = int(input())
  
  if x == 0:
    if len(heap):
      print(len(heap))
      print(heapq.heappop(heap))
    else:
      print(0)  
  else:
    heapq.heappush(heap, x)