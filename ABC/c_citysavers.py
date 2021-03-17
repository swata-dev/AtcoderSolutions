n = int(input())
monsters = list(map(int, input().split()))
heroes = list(map(int, input().split()))
c = 0
for i in range(n):
  c += min(monsters[i]+monsters[i+1],heroes[i])
  monsters[i+1] -= min(max(heroes[i]-monsters[i],0),monsters[i+1])

print(c)