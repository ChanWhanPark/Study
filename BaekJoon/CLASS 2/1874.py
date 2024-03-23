N = int(input())

stack = []
ans = []
find = True
current = 1
for _ in range(N):
  num = int(input())
  
  while current <= num:
    stack.append(current)
    current += 1;
    ans.append("+")
  
  if stack[-1] == num:
    stack.pop()
    ans.append("-")
  else:
    find = False
    

if find == False:
  print("NO")
else:
  for i in ans:
    print(i)
    