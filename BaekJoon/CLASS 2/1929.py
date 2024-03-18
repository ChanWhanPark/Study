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
    
    
'''
M = 1, N = 4
1 continue
2 => for j in range(2, 2)
3 => for j in range(2, 2)
4 => for j in range(2, 3)
...
9 => for j in range(2, 4)
...
16 => for j in range(2, 5)
이런 식으로 탐색 범위를 좁힘.

에라토스테네스의 체
https://ko.wikipedia.org/wiki/%EC%97%90%EB%9D%BC%ED%86%A0%EC%8A%A4%ED%85%8C%EB%84%A4%EC%8A%A4%EC%9D%98_%EC%B2%B4
'''