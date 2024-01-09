## 10773. 제로 (2024.1.9) / S4
T = int(input())
num = [];

for i in range(T):
  n = int(input());
  if (n == 0): num.pop();
  else: num.append(n);
  
print(sum(num))