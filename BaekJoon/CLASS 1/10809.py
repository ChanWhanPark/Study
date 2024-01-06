### 10809. 알파벳 찾기 (2024.1.4) / B2
string = input()

idx = 0;
result = [-1] * 26;
for s in string:
  if (result[ord(s) - 97] == -1):
    result[ord(s) - 97] = idx
  idx += 1
  

for r in result:
  print(r, end=" ")