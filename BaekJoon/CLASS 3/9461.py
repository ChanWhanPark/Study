## 9461. 파도반 수열 (2024.4.23) | S3
T = int(input())

for _ in range(T):
  n = int(input())
  
  dp = [0] * (n + 1);
  
  '''
  Pattern
  dp[1] = 1
  dp[2] = 1
  dp[3] = 1
  dp[4] = 2 = dp[1] + dp[3]
  dp[5] = 2
  dp[6] = 3 = dp[1] + dp[5]
  dp[7] = 4 = dp[2] + dp[6]
  dp[8] = 5 = dp[3] + dp[7]
  dp[9] = 7 = dp[4] + dp[8]
  dp[10] = 9 = dp[9] + dp[5]
  dp[11] = 12 = dp[10] + dp[6]
  dp[12] = 16 = do[11] + dp[7]
  .
  .
  .
  i >= 6에서 dp[i] = dp[i-1] + dp[i-5]
  '''
  
  for i in range(1, n+1):
    if i <= 3:
      dp[i] = 1
    elif i == 4 or i == 5:
      dp[i] = 2
    elif i >= 6:
      dp[i] = dp[i-1] + dp[i-5]
      
  print(dp[n])