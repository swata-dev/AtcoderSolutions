n,k = map(int, input().split())

trees = [int(input()) for _ in range(n)]
trees = sorted(trees)
short = 10**9

for i in range(0,n-k+1):
  if min(short, trees[i+k-1]-trees[i]) != short:
    short = trees[i+k-1]-trees[i]

print(short)