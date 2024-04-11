## 1003. 피보나치 함수 (2024.4.11) | S3
T = int(input())

d = [-1] * 41;
d[0], d[1] = 0, 1;
zero_count = [0] * 41;
zero_count[0] = 1
one_count = [0] * 41;
one_count[1] = 1

# fibo(n)의 0 횟수 = fibo(n-2)의 0 횟수 + fibo(n-1)의 0 횟수
'''
        0 1 fibo(n)
fibo(0)  1 0 0
fibo(1)  0 1 1
fibo(2)  1 1 1
fibo(3)  1 2 2
fibo(4)  2 3 3
'''

def fibo(n):
  if d[n] != -1:
    return
  
  for i in range(2, n+1):
    d[i] = d[i-1] + d[i-2]
    zero_count[i] = zero_count[i-1] + zero_count[i-2];
    one_count[i] = one_count[i-1] + one_count[i-2];

answer = [];

for _ in range(T):
  n = int(input())
  
  fibo(n)
      
  print(zero_count[n], one_count[n])