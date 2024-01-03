### 3052. 나머지 (2024.1.3) / B2

count = 0;
mod = [0] * 42;

for i in range(10):
  A = int(input());
  idx = A % 42;
  mod[idx] += 1

for i in range(len(mod)):
  if (mod[i] != 0):
    count += 1;

print(count);