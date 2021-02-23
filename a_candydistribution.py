n,x = map(int, input().split())
children = list(map(int,input().split()))
children.sort()
cnt = 0

for child in children:
  if x < child:
    break
  x -= child
  cnt += 1
else:
  if x > 0:
    cnt -=1

print(cnt)