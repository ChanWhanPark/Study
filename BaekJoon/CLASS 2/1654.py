# 1654. 랜선 자르기 (2024.3.16) | S2
K, N = map(int, input().split())
lansunList = [];

for _ in range(K):
  lansunList.append(int(input()));
  
start = 1
end = max(lansunList)

while start <= end:
  mid = (start + end) // 2 # 중간 위치 설정
  lines = 0 # 랜선 개수 초기화
  for lan in lansunList:
    lines += ( lan // mid ) # 분할 된 랜선 수
    
  if lines >= N: # 랜선의 개수가 분기점이 됨.
    start = mid + 1
  else:
    end = mid - 1
    
print(end) # start > end인 경우에 end 값에 랜선 길이의 최대값이 들어감