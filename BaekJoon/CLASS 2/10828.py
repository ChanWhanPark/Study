## 10828. 스택 (2024.2.25) | S4
import sys;

T = int(input());
number = [];
for _ in range(T):
  order = sys.stdin.readline().split();
  if (order[0] == 'push'):
    number.append(order[1]);
  elif (order[0] == 'pop'):
    if (len(number) == 0): print(-1)
    else: 
      print(number[len(number)-1])
      number.pop(len(number) - 1)
  elif (order[0] == 'size'):
    print(len(number));
  elif (order[0] == 'empty'):
    if (len(number) == 0): print(1)
    else: print(0)
  elif (order[0] == 'top'):
    if (len(number) == 0): print(-1)
    else: print(number[len(number)-1])
    