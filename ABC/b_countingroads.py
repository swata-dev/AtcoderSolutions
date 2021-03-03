import itertools as it

n,m = map(int, input().split())
roads = []

for i in range(m):
  roads.append(list(map(int, input().split())))

roads = list(it.chain.from_iterable(roads))

for i in range(1,n+1):
  print(roads.count(i))


