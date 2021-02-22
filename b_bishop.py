h, w = map(int, input().split())
if h == 1 or w == 1:
  print(1)
else:
  movable = int(h*w/2)
  print(movable) if h*w % 2 == 0 else print(movable+1)
