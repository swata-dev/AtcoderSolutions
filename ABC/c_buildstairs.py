n = int(input())
h = list(map(int, input().split()))
step = 0

for i in h:
  if step > i:
    print('No')
    exit()
  if step < i:
    step = i-1

print('Yes')