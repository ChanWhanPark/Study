## 5430. AC (2024.7.22) | G5
import sys
from collections import deque
input = sys.stdin.readline
T = int(input())

for _ in range(T):
  P = input()
  N = int(input())
  arr = input().strip()
  arr_list = deque(arr[1:-1].split(','))
  
  if N == 0:
    arr_list = deque()
  
  R = 0 # FOR R COUNT (R이 짝수번이면 뒤집을 필요가 없음)
  error_flag = False # For Error Check
  for p in P:
    if p == 'R':
      R += 1
    elif p == 'D':
      if len(arr_list) == 0:
        print("error")
        error_flag = True
        break
      else:
        if R % 2 == 0:
          arr_list.popleft()
        else:
          arr_list.pop() ## reverse 할 필요 없이 가장 뒤를 꺼냄
        
  if error_flag == True:
    continue
  else:
    if R % 2 == 0: ## Reverse 시키지 않아도 됨
      print('[' + ",".join(arr_list) + ']') # '구분자'.join(list) - 문자열을 구분자 기준으로 합쳐줌
    else: ## Reverse 시켜야 함
      arr_list.reverse()
      print('[' + ",".join(arr_list) + ']')