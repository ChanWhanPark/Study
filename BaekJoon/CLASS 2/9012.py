## 9012. 괄호 (2024.1.9) / S4
T = int(input())
strList = [];
resultList = [];
for i in range(T):
  string = input();
  strList.append(string);

for i in range(T):
  flag = 0;
  for s in strList[i]:
    if s == "(":
      flag += 1;
    else:
      flag -= 1;

    if (flag < 0):
      break;

  if (flag == 0):
    resultList.append('YES');
  else:
    resultList.append('NO');

for i in range(T):
  print(resultList[i]);