n,a,b = map(int, input().split())
sums = 0

for i in range(n+1):
  list = []
  num = i
  sum = 0
  while i > 0:
    list.append(i%10)
    i //= 10
  for j in list:
    sum += j

  if sum >= a and sum <= b:
    sums += num

print(sums)