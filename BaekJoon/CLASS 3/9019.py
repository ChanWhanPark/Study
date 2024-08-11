## 9019. DSLR (2024.8.11) | G4
from collections import deque
T = int(input())

for _ in range(T):
  A, B = map(int, input().split())
  
  visited = [False for i in range(10001)]
  deq = deque()
  deq.append([A, ''])
  visited[A] = True
  
  while deq:
    num, command = deq.popleft()
    
    if num == B:
      print(command)
      break
    
    D = (num * 2) % 10000
    if not visited[D]:
      visited[D] = True
      deq.append([D, command + 'D'])
      
    S = (num - 1) % 10000
    if not visited[S]:
      visited[S] = True
      deq.append([S, command + 'S'])
      
    L = (num // 1000) + (num % 1000) * 10
    if not visited[L]:
      visited[L] = True
      deq.append([L, command + 'L'])
      
    R = num // 10 + (num % 10) * 1000
    if not visited[R]:
      visited[R] = True
      deq.append([R, command + 'R'])