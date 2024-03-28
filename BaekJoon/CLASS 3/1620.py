## 1620. 나는야 포켓몬 마스터 이다솜 (2024.3.28) | S4
def find_value(list, input_value):
  for key, value in list.items():
    if str(key) == input_value:
      return value;
    elif value == input_value:
      return int(key)

N, M = map(int, input().split());
pokemon = {};
for i in range(N):
  p = input()
  pokemon[i+1] = p;
  
for _ in range(M):
  order = input()
  print(find_value(pokemon, order));