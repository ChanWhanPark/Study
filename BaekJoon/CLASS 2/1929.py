## 1929. 소수 구하기 (2024.1.9) / S3 / 시간초과
M, N = map(int, input().split());


for i in range(M, N + 1):
  if i == 1: # 1은 소수가 아니므로 제외
    continue
  for j in range(2, int(i ** 0.5) + 1): 
    # 특정 수의 제곱근을 구해, 그 제곱근까지의 약수를 구하면 
    # 해당 약수를 포함한 수를 모두 제거할 수 있음.
    if i % j == 0: # 약수가 존재하므로 소수가 아님
      break
  else:
    print(i)