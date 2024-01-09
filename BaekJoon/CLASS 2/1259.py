## 1259. 팰린드롬수 (2024.1.10) / B1

while (1):
  num = input();
  flag = 0;
  if (num == '0'): break;
  for i in range(0, len(num)):
    if (num[i] != num[len(num) - (i+1)]):
      flag = 1;
      break;

  if (flag == 1): print("no");
  else: print("yes");