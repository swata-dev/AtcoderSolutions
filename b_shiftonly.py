n =int(input())
ary = list(map(int, input().split()))
count = 0


while all(a % 2 == 0 for a in ary):
  ary = [a/2 for a in ary]
  count += 1

print(count)