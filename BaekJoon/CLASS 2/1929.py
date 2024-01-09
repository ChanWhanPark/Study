## 1929. 소수 구하기 (2024.1.9) / S3 / 시간초과
M, N = map(int, input().split());


for i in range(M, N):
  flag = 1;
  if i == 1:
    print(i)
  else:
    for j in range(2, i):
      if i % j == 0:
        flag = 0;
        break;
    if (flag == 1):
      print(i);