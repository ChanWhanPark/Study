## 1676. 팩토리얼 0의 개수 (2024.1.8) / S5

T = int(input());
factorial = T;
for i in range(T - 1, 0, -1):
  factorial *= i;

factorial_str = str(factorial);
count = 0;

for i in range(len(factorial_str) - 1, 0, -1):
  if int(factorial_str[i]) == 0:
    count += 1;
  else:
    break;

print(count);