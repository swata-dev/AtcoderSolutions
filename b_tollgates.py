n,m,x = map(int,input().split())
gates = list(map(int,input().split()))
count=0

for i in range(x):
  if i in gates:
    count += 1

print(min(count, m-count))