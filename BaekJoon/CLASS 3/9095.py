## 9095. 1, 2, 3 더하기 (2024.4.19) | S3
T = int(input())

"""
Pattern
dp[1] = 1
dp[2] = 2 (1+1, 2)
dp[3] = 4 (1+1+1, 1+2, 2+1, 3)
dp[4] = 7 (1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 2+2, 1+3, 3+1)
dp[5] = 13 (1+1+1+1+1, 1+1+1+2 (4개), 1+1+3 (3개), 2+2+1 (3개), 3+2 (2개))

...
n >= 4에서 dp[n] = dp[n-1] + dp[n-2] + dp[n-3]
"""

for _ in range(T):
  N = int(input());
  dp = [0] * (N+1);
  
  for i in range(1, N+1):
    if i == 1:
      dp[i] = 1
    elif i == 2:
      dp[i] = 2
    elif i == 3:
      dp[i] = 4
    else:
      dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
      
  print(dp[N])