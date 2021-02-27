n, a, b = map(int, input().split())
s = list(input())
passed = 0
foreign = 0

for i in range(n):
  if s[i] == 'a' and passed < a+b:
    print('Yes')
    passed += 1
  elif s[i] == 'b' and passed < a+b and foreign < b:
    print('Yes')
    passed += 1
    foreign += 1
  else:
    print('No')