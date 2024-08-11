## 7662. 이중 우선순위 큐 (2024.8.4) | G4
import heapq

# 삭제할 데이터가 있는지 확인
def isEmpty(nums):
  for item in nums:
    # dictonary인 nums에 데이터가 하나라도 있으면 비어있지 않은 것을 의미함
    if item[1] > 0:
      return False
  
  return True

T = int(input())

for _ in range(T):
  min_heap = [] # 값이 작을수록 높은 우선순위를 가짐
  max_heap = [] # 값이 클수록 높은 우선순위를 가짐
  nums = dict()
  k = int(input())
  for _ in range(k):
    DorI, n = input().split()
    num = int(n)
    
    if DorI == 'I':
      # 중복 삽입이라면
      if num in nums:
        nums[num] += 1
      # 처음 삽입했다면
      else:
        nums[num] = 1
        # 최소 heap에 추가
        heapq.heappush(min_heap, num)
        # 최대 heap에 추가
        heapq.heappush(max_heap, -num)
        
    else:
      # 큐가 비어있지 않을 때만 동작
      if not isEmpty(nums.items()):
        # 최댓값 제거
        if num == 1:
          while -max_heap[0] not in nums or nums[-max_heap[0]] < 1:
            temp = -heapq.heappop(max_heap)
            if temp in nums:
              del(nums[temp])
          nums[-max_heap[0]] -= 1
        # 최솟값 제거
        else:
          while min_heap[0] not in nums or nums[min_heap[0]] < 1:
            temp = heapq.heappop(min_heap)
            if temp in nums:
              del(nums[temp])
          nums[min_heap[0]] -= 1
          
  # 결과 출력           
  if isEmpty(nums.items()):
    print('EMPTY')
  else:
    while min_heap[0] not in nums or nums[min_heap[0]] < 1:
      heapq.heappop(min_heap)
    while -max_heap[0] not in nums or nums[-max_heap[0]] < 1:
      heapq.heappop(max_heap)
    print(-max_heap[0], min_heap[0])