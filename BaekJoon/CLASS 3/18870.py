## 18870. 좌표 압축 (2024.5.31) | S2
N = int(input())
arr = list(map(int, input().split()))

sorted_arr = sorted(list(set(arr)));
# 중복 없이 정렬 [-10, -9, 2, 4]
dic = { sorted_arr[i] : i for i in range(len(sorted_arr))}
# dictionary로 전환 {-10: 0, -9: 1, 2: 2, 4: 3}

for i in arr:
  print(dic[i], end=' ')