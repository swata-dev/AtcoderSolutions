s = list(input())
flag = False

for l in s:
  count = 0
  for i in range(len(s)):
    if l == s[i]:
      count+=1
  if count >= 2:
    flag = True

if flag:
  print('no')
else:
  print('yes')