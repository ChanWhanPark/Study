## 1966. 프린터 큐 (2024.3.12) | S3
import sys
T = int(input());

for _ in range(T):
  N, M = map(int, input().split());
  
  # 중요도
  priority = list(map(int, sys.stdin.readline().split()));
  count = 0;
  
  while priority:
    best = max(priority) # 최댓값 중요도가 제일 높음.
    front = priority.pop(0)
    M -= 1; # 위치를 한 칸 당김
    
    if best == front: # 뽑은 숫자가 제일 큰 숫자일 때,
      count += 1 # 순번 추가
      if M < 0: # 내가 원했던 숫자를 찾음.
        print(count)
        break;
    else: # 뽑은 숫자가 제일 큰 숫자가 아니면
      priority.append(front)
      if M < 0: # 제일 앞에서 뽑힌 것이었으면
        M = len(priority) - 1; # 제일 뒤로 이동
        
  
  
  
  '''
  ex) 중요도가 2, 1, 4, 3인 priority에서 0번 인덱스가 몇 번째로 뽑히는지 알고싶음.
  입력 : N = 4, M = 0, priority = [2, 1, 4, 3]
  1. max(priority) = 4
    pop(0) -> 2가 뽑힘, else문에 걸림, 다시 배열의 맨 뒤로 들어감, M = -1이므로, M = 3으로 바뀜
    pop(0) -> 1이 뽑힘, else문에 걸림, 다시 배열의 맨 뒤로 돌아감, M = 2
    pop(0) -> 4가 뽑힘, count += 1, M = 2 (내가 원하는 위치가 아님)
    
  2. max(priority) = 3
    pop(0) -> 2가 뽑힘, else문에 걸림, 다시 배열의 맨 뒤로 돌아감, M = 1
    pop(0) -> 1이 뽑힘, else문에 걸림, 다시 배열의 맨 뒤로 돌아감, M = 0
    pop(0) -> 3이 뽑힘, count += 2, M = 0 (내가 원하는 위치가 아님)
    
  3. max(priority) = 2
    pop(0) -> 2가 뽑힘, count += 3, M = -1, print 후 break;
  '''
  
  