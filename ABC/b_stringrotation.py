s = input()
t = input()

for i in range(len(s)):
  rotated = s[i:len(s)] + s[:i]
  if rotated == t:
    print('Yes')
    exit()
print('No')