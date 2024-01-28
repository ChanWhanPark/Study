## 7568. 덩치 (2024.1.28) | S5
T = int(input());
personList = [];

for _ in range(T):
  weight, height = map(int, input().split());
  personList.append([weight, height]);

for w in personList: # 몸무게 비교용
  rank = 1;
  for h in personList: # 키 비교용
    if w[0] < h[0] and w[1] < h[1]: # 몸무게와 키가 모두 클 때,
      rank += 1;

  print(rank, end=" ");