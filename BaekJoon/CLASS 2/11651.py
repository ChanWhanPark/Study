## 11651. 좌표 정렬하기 2 (2024.1.30) | S5
def quick_sort(arr):
  if len(arr) <= 1:
    return arr;

  pivot = arr[len(arr) // 2];
  left = [element for element in arr if element < pivot];
  middle = [element for element in arr if element == pivot];
  right = [element for element in arr if element > pivot];

  return quick_sort(left) + middle + quick_sort(right);

T = int(input());
coordList = [];

for _ in range(T):
  x, y = map(int, input().split());
  coordList.append([y, x]);

sorted_list = quick_sort(coordList);

for y, x in sorted_list:
  print(x, y)