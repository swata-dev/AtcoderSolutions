import math

a = int(input())
b = int(math.sqrt(a))

for i in range(b+1,0,-1):
  if a % i == 0:
    x = a / i
    y = a / x
    print(int(x+y-2))
    break