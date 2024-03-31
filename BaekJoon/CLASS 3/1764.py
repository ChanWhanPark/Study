## 1764. 듣보잡 (2024.3.31) | S4
N, M = map(int, input().split())

no_listen = set()
no_see = set()

for _ in range(N):
  no_listen.add(input())
  
for _ in range(M):
  no_see.add(input())
  
no_listen_see = list()

for name in no_listen:
  if name in no_see:
    no_listen_see.append(name)
    
print(len(no_listen_see))
no_listen_see.sort()
for name in no_listen_see:
  print(name)