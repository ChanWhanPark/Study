## 11723. 집합 (2024.3.28) | S5
import sys

def check(list, num):
  if num in list:
    return True;
  else:
    return False;

M = int(input());
S = [0] * 20;

for _ in range(M):
  order = sys.stdin.readline().split();
  if (order[0] == "add"):
    num = int(order[1]);
    S[20 - num] = 1;
  elif (order[0] == "remove"):
    num = int(order[1]);
    S[20 - num] = 0;
  elif (order[0] == "check"):
    num = int(order[1]);
    if (S[20 - num] == 1):
      print(1)
    else:
      print(0)
  elif (order[0] == "toggle"):
    num = int(order[1]);
    if (S[20 - num] == 1):
      S[20 - num] = 0;
    else:
      S[20 - num] = 1;
  elif (order[0] == "all"):
    S = [1] * 20;
  elif (order[0] == "empty"):
    S = [0] * 20;

