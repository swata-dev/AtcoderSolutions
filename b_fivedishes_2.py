menu = [int(input()) for i in range(5)]
last = 0
total = []

for i in range(5):
  surplus = menu[i] % 10
  if surplus != 0 and 10 - surplus > last:
    last = 10 - surplus
  if surplus == 0:
    surplus = 10
  total.append(menu[i]+10-surplus)

print(sum(total)-last)
