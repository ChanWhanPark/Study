## 1546. 평균 (2024.1.6) / B1
N = int(input());
score = list(map(int, input().split()));

max = max(score);

for i in range(N):
  score[i] = score[i] / max * 100;

print(sum(score) / N);