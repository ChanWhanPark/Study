# 11726. 2xn 타일링 (2024.4.23) | S3
N = int(input())
dp = [0] * (N+1)

'''
Pattern
dp[1] = 1
dp[2] = 2
dp[3] = 3
dp[4] = 5
...
dp[n] = dp[n-1] + dp[n-2]
'''
for i in range(1, N+1):
  if i == 1:
    dp[1] = 1
  elif i == 2:
    dp[2] = 2
  else:
    dp[i] = dp[i-1] + dp[i-2]
    
print(dp[i] % 10007)