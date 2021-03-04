n = int(input())
time = list(map(int,input().split()))
m = int(input())
drinks = []
for i in range(m):
  drinks.append(list(map(int,input().split())))

for i in range(m):
  after = time.copy()
  after[drinks[i][0]-1] = drinks[i][1]
  print(sum(after))