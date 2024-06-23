## 5525. IOIOI (2024.6.23) | S1

N = int(input())
M = int(input())
S = input()

i = 0
IOI_COUNT = 0
result = 0

while i < (M - 1): ## Index 기준
  if S[i:i+3] == 'IOI': # IOI를 찾으면
    i += 2 # 다다음 인덱스로 넘어감
    IOI_COUNT += 1
    if IOI_COUNT == N: # 다 찾았으면
      result += 1 # 문자열을 한 번 찾았으므로 더함
      IOI_COUNT -= 1 # count는 하나 제거 (중복)
  else:
    i += 1
    IOI_COUNT = 0
    
print(result)