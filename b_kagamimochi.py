n = int(input())
mochi = []

for i in range(n):
  mochi.append(int(input()))

print(len(list(set(mochi))))