## 11866. 요세푸스 문제 0 (2024.1.30) | S5
N, K = map(int, input().split());
integerList = [i + 1  for i in range(N)];
result = [];
param = K - 1;

while len(integerList) > 0:
  for _ in range(param):
    integerList.append(integerList[0]);
    integerList.pop(0);
  result.append(integerList[0]);
  integerList.pop(0);

print("<", end="");
for i in range(len(result)):
  if (i == len(result) - 1):
    print(result[i], end="");
  else:
    print(result[i], end=", ");
print(">")