## 6064. 카잉 달력 (2024.6.30) | S1
### 중국인의 나머지 정리? - 연립 합동식
#### 합동식: (a-b)가 m으로 나누어 떨어질 때: a는 m에 대하여 b와 합동임.
### C = A(modB)라면, 일반적인 방정식으로는 C = Bk + A로 나타낼 수 있으며, B | C-A로 나타낼 수 있음.
### 즉, (C-A)는 B로 나눠떨어짐.

### 탐색 시간을 줄이는 방법 -> day의 탐색 시간을 줄여야 함
### 규칙 : day는 x + M*i 이거나 y + N*j이다.

T = int(input());
resultArr = []

for _ in range(T):
  M, N, x, y = map(int, input().split())
  
  result = -1
  
  mORn = M if M > N else N
  xORy = x if mORn == M else y
  
  if x == y: # x와 y 값이 같다면, day=x=y
    result = x
  else:
    day = xORy
    while day <= M*N:
      if (day - x) % M == 0 and (day - y) % N == 0:
        result = day
        break;
      day += mORn;
      
  print(result)
      
