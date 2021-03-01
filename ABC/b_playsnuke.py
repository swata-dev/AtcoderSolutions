n = int(input())
m = 10**9+1

for i in range(n):
  a,p,x = map(int,input().split())
  if x-a > 0:
    m = min(m, p)

print(-1 if m == 10**9+1 else m)