import itertools
menu = [int(input()) for i in range(5)]

patterns = [v for v in itertools.permutations(menu)]
totals = []

for pattern in patterns:
  total = 0
  for i in range(4):
    total += pattern[i]
    surplus = total % 10
    if surplus != 0:
      total += (10 - surplus)
  total += pattern[4]
  totals.append(total)

print(min(totals))