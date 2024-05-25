## 1541. 잃어버린 괄호 (2024.5.19) | S2
'''
최솟값 : 문자열에서 - 기호를 만날 때, 
다음 마이너스까지 그 사이에 있는 수를 모두 더하고 마지막에 빼줌.
'''
math_string = input().split('-');
num = 0
print(math_string)

for i in math_string[0].split('+'):
  print(i)
  num += int(i)
  
for i in math_string[1:]:
  print(i)
  for j in i.split('+'):
    print(j)
    num -= int(j)
    
print(num);