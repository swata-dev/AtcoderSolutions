n,m =map(int,input().split())
low, high = map(int, input().split())

for _ in range(m-1):
  less, more = map(int, input().split())
  low = max(low, less)
  high  = min(high, more)

print(max(0, high-low+1))