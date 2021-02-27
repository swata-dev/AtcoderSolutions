a, b = map(int, input().split())
count = 0
sum = 1

while sum < b:
  sum += a - 1
  count += 1

print(count)
