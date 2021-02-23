a,b,c = map(int, input().split())

if a == b == c:
  if a % 2 == 0:
    print(-1)
  else:
    print(0)
else:
  count = 0
  while a%2 == 0 and b%2 == 0 and c%2 == 0:
    ax = b//2 + c//2
    bx = c//2 + a//2
    cx = a//2 + b//2

    count += 1

    a,b,c = ax,bx,cx

  print(count)
