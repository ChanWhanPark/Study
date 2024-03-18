## 2108. 통계학 (2024.3.16) | S3
N = int(input());
numList = [];
for _ in range(N):
  numList.append(int(input()));
  
numList.sort()
sum = sum(numList);
length = len(numList);

# 1. 산술평균
'''
def myRound(number):
  if number - int(number) >= 0.5:
    return int(number) + 1;
  else:
    return int(number);
'''

print(round(sum / length));

# 2. 중앙값
print(numList[length // 2])
  
# 3. 최빈값
freqList = dict() # Dictionary
freqMaxList = []
for i in numList:
  if i in freqList:
    freqList[i] += 1
  else:
    freqList[i] = 1
  
freqMax = max(freqList.values()) # 최댓값 구함
  
for i in freqList:
  if freqMax == freqList[i]:
    freqMaxList.append(i)
    
if (len(freqMaxList) > 1): # 여러개면
  print(freqMaxList[1]); # 두 번째로 작은 값
else:
  print(freqMaxList[0])

# 4. 범위
print(numList[-1] - numList[0])