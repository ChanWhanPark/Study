## 2577. 숫자의 개수 (2024.1.2) / B2

a = int(input());
b = int(input());
c = int(input());

result = a * b * c;
result_string = str(result);

result_value = [0] * 10;

for r in result_string:
  result_value[int(r)] += 1;

for i in range(0, 10):
  print(result_value[i]);