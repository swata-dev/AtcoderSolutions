s = list(input())
count = 0
new = ''
following = ''

for i in range(len(s)):
  new += s[i]
  if new != following:
    following = new
    new = ''
    count += 1

print(count)