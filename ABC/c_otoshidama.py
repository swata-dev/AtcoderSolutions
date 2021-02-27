x, y = map(int, input().split())

for i in range(x+1):
  for j in range(x-i+1):
    k = x - i - j
    if 0 <= k <= 2000 and 1000*i+5000*j+10000*k == y:
      print(k, j, i)
      exit()

print(-1, -1, -1)