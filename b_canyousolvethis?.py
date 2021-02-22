n, m, c = map(int, input().split())
bs = list(map(int, input().split()))
a_list = []

for i in range(n):
  a_list.append(list(map(int,input().split())))

count = 0

for i in range(n):
  sum = c
  for j in range(m):
    sum += a_list[i][j]*bs[j]
  if sum > 0:
    count+= 1

print(count)