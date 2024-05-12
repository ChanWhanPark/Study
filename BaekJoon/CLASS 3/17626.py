## 17626. Four Squares (2024.5.12) | S3
'''
Pattern
1 -> 1 2 -> 2 (d[1]+d[1]) 3 -> 3 (d[1]+d[1]+d[1])
4 -> 1 5 -> 2 (d[4]+d[1]) 6 -> 3 (d[4]+d[1]+d[1]) 7 -> 3(d[4]+d[1]+d[1]+d[1]) 
8 -> 2 d[4] + d[4]
9 -> 1 10 -> d[9]+d[1]

제곱수는 무조건 1
그 외는 dp[n] = dp[n] + dp[n - (최댓값)**2]
'''

N = int(input())
dp = [0] * (N + 1)

k = 1
while k ** 2 <= N:
  dp[k ** 2] = 1
  k += 1

for i in range(1, N+1):
  if dp[i] != 0:
    continue
  j = 1
  while j**2 <= i:
    if dp[i] == 0:
      dp[i] = dp[j**2] + dp[i - j**2]
    else:
      dp[i] = min(dp[i], dp[j**2] + dp[i - j**2])
    j += 1
    
print(dp[N])