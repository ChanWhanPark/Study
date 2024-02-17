## 2164. 카드 2 (2024.2.17) | S4
from collections import deque

N = int(input())
card = deque([ i + 1 for i in range(N)])
inputNumber = 0;
while (len(card) > 1):
  card.popleft();
  card.append(card.popleft());
  
print(card[0]);