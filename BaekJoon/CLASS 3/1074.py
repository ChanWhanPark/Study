# 1074. Z (2024.6.3)
def visited(n, r, c):
  global res
  
  # 찾는 좌표라면 res를 출력하고 종료함
  if r == R and c == C:
    print(int(res))
    return
  
  # 탐색 중인 배열 중에 찾는 좌표가 없으면 좌표에 크기를 더함
  if not (r <= R < r+n and c <= C < c+n):
    res += n ** 2
    return
  
  # 네 개의 사분면을 재귀적으로 탐색
  visited(n // 2, r, c) # 1사분면
  visited(n // 2, r, c + n // 2) # 2사분면
  visited(n // 2, r + n // 2, c) # 3사분면
  visited(n // 2, r + n // 2, c + n // 2) # 4사분면

N, R, C = map(int, input().split())
res = 0

visited(2 ** N, 0, 0)