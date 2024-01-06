## 1157. 단어 공부 (2024.1.5) / B1

string = input()

result = [0] * 26;

for s in string:
  if ord(s) >= 65 and ord(s) < 97:
    result[ord(s)-65] += 1;
  elif ord(s) >= 97:
    result[ord(s)-97] += 1;


max_idx = 0;
max_value = 0;
duplicate_flag = 0;

for i in range(0, len(result)):
  if result[i] > max_value:
    max_idx = i;
    max_value = result[i];
    duplicate_flag = 0;
  elif result[i] == max_value:
    duplicate_flag = 1;

if (duplicate_flag):
  print("?");
else:
  print(chr(max_idx + 65));