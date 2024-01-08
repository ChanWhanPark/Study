## 1978. 소수 찾기 (2024.1.8) / B2
T = int(input())
num = list(map(int, input().split()))

flag = 1;
count = 0;

for i in range(T):
  if (num[i] > 1):
    for j in range(2, num[i]):
      if num[i] % j == 0:
        flag = 0;
        break;
  else:
    flag = 0;

  if (flag == 1): count += 1;
  else: flag = 1;

print(count);
    