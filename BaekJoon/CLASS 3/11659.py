## 11659. 구간 합 구하기 4 (2024.4.23) | S3
N, M = map(int, input().split());
numberList = list(map(int, input().split()))
sumList = [0] # 구간 합 공식 구현 위함
sumVal = 0;
for i in numberList:
  sumVal += i
  sumList.append(sumVal);
  
'''
1 - 3 : S[1] + S[2] + S[3]
2 - 4 : S[1] + S[2] + S[3] + S[4] - ( S[1] )
3 - 4 : S[1] + S[2] + S[3] + S[4] - ( S[1] + S[2] )

구간 합 : S[end] - S[start - 1]
'''

for _ in range(M):
  start, end = map(int, input().split())
  
  print(sumList[end] - sumList[start - 1])