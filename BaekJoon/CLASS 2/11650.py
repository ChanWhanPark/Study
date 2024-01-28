## 11650. 좌표 정렬하기 (2024.1.28) | S5
def quick_sort(points):
  if len(points) <= 1:
    return points;

  pivot = points[len(points) // 2] # 피벗 설정
  left = [element for element in points if element < pivot];
  middle = [element for element in points if element == pivot];
  right = [element for element in points if element > pivot];

  return quick_sort(left) + middle + quick_sort(right); 
# 재귀적으로 수행하여 마지막에는 middle만 반환

T = int(input());

points = [];
for i in range(T):
  x, y = map(int, input().split());
  points.append([x, y]);

sorted_point = quick_sort(points);

for x, y in sorted_point:
  print(x, y)

'''
# 버블 정렬
for i in range(T):
  for j in range(T - i - 1):
    if (points[j] > points[j + 1]): # x좌표가 증가하는 순서, x좌표가 동일하면 y좌표 증가
      points[j], points[j+1] = points[j + 1], points[j];


for x, y in points:
  print(x, y)
'''