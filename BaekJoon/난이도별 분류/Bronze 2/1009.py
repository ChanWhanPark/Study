## 1009. 분산처리 (2024.1.22) | B2
T = int(input());

'''
시간 초과
for i in range(T):
  a, b = map(int, input().split());
  c = str(a ** b);
  print(int(c[len(c) - 1]));
'''