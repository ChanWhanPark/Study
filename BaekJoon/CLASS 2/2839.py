## 2839. 설탕 배달 (2024.2.17) | S4
N = int(input())

result = 0

while N >= 0:
  if N % 5 == 0:
    result += (N // 5) # 5의 배수일 시, 5로 나눈 몫을 구하면 정수가 됨
    print(result)
    break;
  N -= 3;
  result += 1;
else: # while문이 거짓일 때,
  print(-1);