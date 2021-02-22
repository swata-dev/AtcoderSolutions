n = int(input())
k = int(input())
Xs = list(map(int, input().split()))
dis = 0

for i in range(n):
  dis += 2*Xs[i] if Xs[i] <= k - Xs[i] else 2*(k - Xs[i])

print(dis)