## 10814. 나이순 정렬 (2024.1.28) | S5
def quick_sort(user):
  if len(user) <= 1:
    return user;

  pivot = user[len(user) // 2]
  left = [elem for elem in user if int(elem[0]) < int(pivot[0])]
  middle = [elem for elem in user if int(elem[0]) == int(pivot[0])]
  right = [elem for elem in user if int(elem[0]) > int(pivot[0])]

  return quick_sort(left) + middle + quick_sort(right);


T = int(input());
userList = [];

for _ in range(T):
  x, y = input().split();
  userList.append([x, y]);

sorted_userList = quick_sort(userList);

for age, name in sorted_userList:
  print(age, name);