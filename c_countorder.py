import itertools

n = int(input())
elements = [i for i in range(1,n+1)]
x = tuple(map(int,input().split()))
y = tuple(map(int,input().split()))

all_list = itertools.permutations(elements)

for i,case in enumerate(all_list):
  if x == case:
    x = i
  if y == case:
    y = i

print(abs(x-y))