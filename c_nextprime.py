import math
x = int(input())

for i in range(x, 10**5+4):
  flag = True
  for j in range(2, int(math.sqrt(i))):
    if i % j == 0:
      flag = False
      break
  if flag:
    print(i)
    break