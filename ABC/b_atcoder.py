s = list(input())
count = 0
maxim = 0

for i in range(len(s)):
  if s[i] in 'ACGT':
    count += 1
  else:
    count = 0
  maxim = max(maxim, count)

print(maxim)

