n = int(input())
bricks = list(map(int,input().split()))
breaks = 0
idx = 1

for i in range(n):
  if bricks[i] == idx:
    idx += 1
  else:
    bricks[i] = 0

if bricks.count(0) == n:
  print(-1)
else:
  print(bricks.count(0))