## 11399. ATM (2024.4.6) | S4
import sys

N = int(input());
ATM = list(map(int, sys.stdin.readline().split()))

ATM = sorted(ATM)

sum = 0
ATM_sum = 0
for time in ATM:
  sum += time
  ATM_sum += sum
  

print(ATM_sum)