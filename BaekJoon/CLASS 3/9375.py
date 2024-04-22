# 9375. 패션왕 신해빈 (2024.4.22) | S3
T = int(input())
for _ in range(T):
  clothes = {} # Dictionary
  result = 1
  n = int(input())
  for _ in range(n):
    name, body = input().split()
    if not body in clothes:
      clothes[body] = 1
    else:
      clothes[body] += 1

  '''
  
  '''

  for i in clothes:
    result *= (clothes[i] + 1) 
    
  print(result - 1) # 모든 옷을 안 입은 경우를 뺌
  
  