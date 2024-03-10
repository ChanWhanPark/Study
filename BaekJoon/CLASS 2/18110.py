## 18110. solved.ac (2024.3.10) | S4
def newRound(val):
  if val - int(val) >= 0.5:
    return int(val) + 1
  else:
    return int(val)

N = int(input());
if N:
  avg = newRound(N * 0.15)

  numList = [];
  for _ in range(N):
    numList.append(int(input()));
    
  numList.sort()

  if avg > 0:
    range = numList[avg:-avg]
    print(newRound(sum(range) / len(range)))
  else: ## avg == 0
    print(newRound(sum(numList) / len(numList)))
else:
  print(0)