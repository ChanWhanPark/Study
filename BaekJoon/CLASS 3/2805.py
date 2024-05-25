## 2805. 나무 자르기 (2024.5.25) | S2
# 1654를 많이 참조함
N, M = map(int, input().split())
trees = list(map(int, input().split()))

start = 1
end = max(trees)

while start <= end:
  mid = (start + end) // 2
  treeLeft = 0
  for tree in trees:
    value = tree - mid
    if value < 0:
      value = 0
    treeLeft += value
    
  if treeLeft >= M:
    start = mid + 1 
  elif treeLeft < M:
    end = mid - 1 
  
    
print(end)
  