## 1931. 회의실 배정 (2024.6.13) | S1

# 최대한 많은 회의를 할 수 있도록 유도해야 함.
## 회의 종료 시간을 기준으로 가장 빠른 회의를 선택
### 종료시간을 기준으로 선택한다면, 종료시간을 기준으로 sort하고 sort된 배열을 순차적으로 확인.
### 1번 회의가 종료되었다면, 다음 회의시간 중 가장 빨리 끝나는 회의를 자동 선택함.

N = int(input())

timeline = [] # 회의 시간 저장
for i in range(N):
  start, end = map(int, input().split())
  timeline.append([start, end])
  
timeline.sort(key=lambda x : [x[1], x[0]]) 
# lambda : [start, end]에서 end를 기준으로 정렬, 그 이후 start 기준으로 정렬
count = 1

end = timeline[0][1]
# 첫 회의의 끝나는 시간을 기준으로 정렬

for i in range(1, N):
  if timeline[i][0] >= end:
    # 두 번째 회의부터 끝나는 시간이 시작시간과 비교할 때,
    # 시작시간이 크거나 같은 경우에 그 회의를 선택함.
    end = timeline[i][1]
    count += 1
    
print(count)