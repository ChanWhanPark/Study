## 1357. 뒤집힌 덧셈 (2024.1.11) / B1
def REV(num):
  result = '';
  for i in range(len(num), 0, -1):
    result += num[i-1];

  return result;

A, B = input().split();
sum = int(REV(A)) + int(REV(B));
result = REV(str(sum))
print(int(result));