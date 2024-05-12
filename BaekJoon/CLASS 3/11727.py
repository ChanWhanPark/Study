## 11727. 2xn 타일링 2 (2024.5.6) | S3
N = int(input())
dp = [0] * (N + 1)

'''
Pattern
dp[1] = 1
dp[2] = 3
dp[3] = 5
dp[4] = 11
...
n >= 4에서 dp[n] = 2 * dp[n-2] + dp[n-1]
'''

for i in range(1, N+1):
  if i == 1:
    dp[i] = 1
  elif i == 2:
    dp[i] = 3
  elif i == 3:
    dp[i] = 5
  else:
    dp[i] = (2 * dp[i-2]) + dp[i-1]
    

print(dp[N] % 10007)