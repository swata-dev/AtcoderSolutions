n = int(input())
d,x= map(int, input().split())
span = [int(input()) for _ in range(n)]

for i in range(n):
  count = 1
  while count <= d:
    count += span[i]
    x += 1

print(x)
