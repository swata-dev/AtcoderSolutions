n = int(input())
sdt = list(map(int,input().split()))
odr = []
for i,j in enumerate(sdt):
  odr.append((j,i+1))
ans = [x for _,x in sorted(odr)]

print(*ans)

