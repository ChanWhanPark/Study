## 4949. 균형잡힌 세상 (2024.1.10) / S4 (예외 케이스 존재 : '([)]')

while (1):
  small_flag = 0;
  big_flag = 0;
  small_or_big = 0;

  string = input();
  if (string == '.'): break;
  else:
    for s in string:
      if (s == "("):
        small_flag += 1;
      elif (s == ")"):
        small_flag -= 1;
      elif (s == "["):
        big_flag += 1;
      elif (s == "]"):
        big_flag -= 1;
  
      if small_flag < 0 or big_flag < 0:
        break;
  
      if small_flag * big_flag < 0:
        break;

  if (small_flag == 0 and big_flag == 0):
    print("yes");
  else:
    print("no")