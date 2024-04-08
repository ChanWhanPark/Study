## 17219. 비밀번호 찾기 (2024.4.6) | S4
import sys
N, M = map(int, input().split())

site = dict()

for _ in range(N):
  info = sys.stdin.readline().split()
  site[info[0]] = info[1]
  
for _ in range(M):
  site_ = input()
  print(site[site_])