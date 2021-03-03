n = int(input())
words = [input() for i in range(n)]
count = 1

for i in range(1,n):
  if not words[i][0] == words[i-1][-1]:
    break
  if words.count(words[i]) != 1:
    break
  count += 1

print('Yes' if count == n else 'No' )