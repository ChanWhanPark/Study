## 2562. 최댓값 (2024.1.5) / B3
max_value = 0;
max_index = 0;

for i in range(9):
  N = int(input());
  if (N > max_value):
    max_value = N;
    max_index = i + 1;

print(max_value);
print(max_index);