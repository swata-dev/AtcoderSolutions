w = list(input())
s = set(w)
flag = True

for l in s:
  if w.count(l) % 2 == 1:
    flag = False

print('Yes' if flag else 'No')
