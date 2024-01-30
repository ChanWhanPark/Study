## 1920. 수 찾기 (2024.1.31) | S4
def find_number(list, start, end, target):
  if start > end:
    return 0;
  
  middle = (start + end) // 2;
  if target == list[middle]: 
    return 1;
  elif target < list[middle]:
    return find_number(list, start, middle - 1, target);
  else:
    return find_number(list, middle + 1, end, target);


N = int(input());
nList = list(map(int, input().split()));
nList.sort()

M = int(input());
mList = list(map(int, input().split()));

for m in mList:
  print( find_number(nList, 0, N- 1, m) );
