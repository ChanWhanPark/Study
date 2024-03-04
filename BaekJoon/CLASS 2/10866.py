## 10866. 덱 (2024.2.25) | S4
from collections import deque
import sys

number = deque()
T = int(input())

for _ in range(T):
  order = sys.stdin.readline().split()
  
  if (order[0] == 'push_front'):
    number.appendleft(order[1])
  elif (order[0] == 'push_back'):
    number.append(order[1])
  elif (order[0] == 'pop_front'):
    if (len(number) == 0): print(-1);
    else:
      print(number[0]);
      number.popleft()
  elif (order[0] == 'pop_back'):
    if (len(number) == 0): print(-1);
    else:
      print(number[-1]);
      number.pop();
  elif (order[0] == 'size'):
    print(len(number));
  elif (order[0] == 'empty'):
    if (len(number) == 0): print(1)
    else: print(0)
  elif (order[0] == 'front'):
    if (len(number) == 0): print(-1)
    else: print(number[0])
  elif (order[0] == 'back'):
    if (len(number) == 0): print(-1)
    else: print(number[-1])