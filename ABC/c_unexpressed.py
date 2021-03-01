n = int(input())
s = set([])

for i in range(2, 10**5+1):
  for j in range(2, 50):
    if i**j <= n:
      s.add(i**j)
    else:
      break

print(n-len(s))