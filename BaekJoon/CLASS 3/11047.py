## 11047. 동전 0 (2024.4.4) | S4
N, K = map(int, input().split())
money = []
for _ in range(N):
  money.append(int(input()))
  
coin = 0;
for i in reversed(range(N)):
  coin += K // money[i];
  K = K % money[i];
  
print(coin)