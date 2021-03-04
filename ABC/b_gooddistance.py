import math

n,d = map(int, input().split())
points = []
count = 0

for i in range(n):
  points.append(list(map(int, input().split())))

for i in range(n-1):
  for j in range(i+1, n):
    variance = 0
    for k in range(d):
      variance += (points[i][k] - points[j][k])**2
    if math.sqrt(variance).is_integer():
      count += 1

print(count)