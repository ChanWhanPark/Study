## 1018. S4

N, M = map(int, input().split())
board = []
for i in range(N):
    board.append(input())
repair = []

for i in range(N-7): # 리스트를 8 * 8로 쪼갬
  for j in range(M-7):
    first_W = 0 # 흰색으로 시작
    first_B = 0 # 검은색으로 시작
    for k in range(i,i+8): # 시작시점 (0 ~ 7)
      for l in range(j,j + 8): # 시작지점 (0 ~ 7)
        if (k + l) % 2 == 0: # 짝수인 경우
          if board[k][l] != 'W': # B이면
            first_W = first_W+1 # W를 칠함
          if board[k][l] != 'B': # W이면
            first_B = first_B + 1 # B로 칠함
        else: # 홀수인 경우
          if board[k][l] != 'B': # B이면
            first_W = first_W+1 # W로 칠함
          if board[k][l] != 'W': # W이면
            first_B = first_B + 1 # B로 칠함
    repair.append(first_W) # W로 칠하는 경우의 수
    repair.append(first_B) # B로 칠하는 경우의 수
        
        
print(min(repair))