a,b,m = map(int,input().split())
As = list(map(int,input().split()))
Bs = list(map(int,input().split()))
combo = [list(map(int,input().split())) for _ in range(m)]

cheapest = min(As)+min(Bs)
for a,b,discount in combo:
  price = As[a-1] + Bs[b-1] - discount
  if price < cheapest:
    cheapest = price

print(cheapest)
