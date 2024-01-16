## 1181. 단어 정렬 (2024.1.16) | S5
T = int(input());
wordList = [];

for i in range(T):
  word = input();
  if word not in wordList:
    wordList.append(word);

wordList.sort();
wordList.sort(key=len);

for s in wordList:
  print(s);