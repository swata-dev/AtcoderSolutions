n = int(input())
num_list = []

for i in range(n):
  num_list.append(list(map(int,input().split())))

count = 0
dt = 0
dx = 0
dy = 0

for i in range(n):
  t = num_list[i][0]
  x = num_list[i][1]
  y = num_list[i][2]

  if abs(x-dx)+abs(y-dy) <= t-dt and t%2 == (x+y)%2:
    count += 1
    dt, dx, dy = t, x, y

if count == n:
  print("Yes")
else:
  print("No")
