## 2751. 수 정렬하기 2 (2024.1.28) | S5
T = int(input());
num = [];

for i in range(T):
  num.append(int(input()));

num.sort();

for n in num:
  print(n);