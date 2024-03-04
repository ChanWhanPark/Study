## 10816. 숫자 카드 2 (2024.3.4) | S4
N = int(input());
a_list = sorted(list(map(int, input().split())));

M = int(input());
b_list = list(map(int, input().split()));

count = {};
for a in a_list:
  if a in count:
    count[a] += 1
  else:
    count[a] = 1
    
    
for b in b_list:
  if b in count:
    print(count[b], end=' ')
  else:
    print(0, end=' ')