n = int(input())
t,a = map(int, input().split())
closest = 0
dif = 10**5+1
cand = list(map(int, input().split()))

for i in range(n):
  if dif > abs(a-(t-cand[i]*0.006)):
    closest = i+1
  dif = min(dif, abs(a-(t-cand[i]*0.006)))

print(closest)