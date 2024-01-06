## 10818. 최소, 최대 (2024.1.6) / B3
N = int(input())
result = list(map(int, input().split()));

max = -1000000
min = 1000000

for r in result:
  if r > max:
    max = r

  if r < min:
    min = r


print(min, end=" ")
print(max)