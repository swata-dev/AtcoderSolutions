k, n = map(int, input().split())
homes = list(map(int, input().split()))
dis = []
for i in range(n):
  x = abs(homes[i]-homes[i-1])
  dis.append(x) if x <= k/2 else dis.append(k - x)

print(k - max(dis))