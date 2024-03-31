## 1620. 나는야 포켓몬 마스터 이다솜 (2024.3.31) | S4
N, M = map(int, input().split());

pokemon = dict();
number = dict();
for i in range(N):
  p = input()
  pokemon[i + 1] = p;
  number[p] = i + 1
  
for _ in range(M):
  find = input()
  if find.isalpha():
    print(number[find])
  else:
    print(pokemon[int(find)])