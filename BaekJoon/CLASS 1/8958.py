## 8958. OX 퀴즈 (2024.1.7) / B2
T = int(input());
quiz = [];
score = 0;
result = [];
O = 0;
for i in range(T):
  quiz.append(input());

for i in range(T):
  for q in quiz[i]:
    if q == 'O':
      O += 1;
    elif q == 'X':
      O = 0;
    score += O;
  result.append(score);
  O = 0;
  score = 0;

for i in range(T):
  print(result[i]);
