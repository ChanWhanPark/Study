## 1152. 단어의 개수 (2024.1.1)
string = input();
length = len(string);
count = 0;

for i in range(0, length):
  if (i != 0):
    if string[i] == " ":
      count += 1;
  if (i == length - 1):
    if string[i] != " ":
      count += 1;

print(count);