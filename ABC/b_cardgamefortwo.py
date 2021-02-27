n = int(input())

cards = list(map(int, input().split()))
cards = sorted(cards)

a = 0
b = 0

for i in range(n):
  if i % 2 == 0:
    a += cards[i]
  else:
    b += cards[i]

print(abs(a - b))