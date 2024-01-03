### 2675. 문자열 반복 (2024.1.3) / B2

T = int(input());
for i in range(T):
  R, S = input().split();
  for s in S:
    for j in range(int(R)):
      print(s, end="");

  print();