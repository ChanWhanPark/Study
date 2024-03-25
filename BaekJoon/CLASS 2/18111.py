## 18111. 마인크래프트 (2024.3.25) | S2
import sys

N, M, B = map(int, input().split()) # N: 세로, M: 가로, B: 높이
field = [list(map(int, sys.stdin.readline().split())) for _ in range(N)] # N번만큼 리스트 입격
height = 0
answer = 500*500*256*2 # 나올 수 있는 최대값

for i in range(257):
  max, min = 0, 0 # max : 1번 작업용, min : 2번 작업용
  for loop_1 in range(N):
    for loop_2 in range(M):
      if field[loop_1][loop_2] >= i: # 현재 높이가 목표 높이보다 높으면
        max += (field[loop_1][loop_2] - i) # 블록을 제거하여 인벤토리에 넣음. 작업 1
      else: # 현재의 높이가 목표 높이보다 낮다면 
        min += (i - field[loop_1][loop_2]) # 블록을 꺼내 현재 높이에 붙임, 작업 2
        
  inven = max + B # 인벤토리로 들어가는 블록의 개수
  if inven < min:
    continue
    
  time = 2 * max + min # 1번 작업은 2초, 2번 작업은 1초 수행
  if time <= answer:
      # 최댓값으로 갱신
    answer = time
    height = i  
      
print(answer, height)