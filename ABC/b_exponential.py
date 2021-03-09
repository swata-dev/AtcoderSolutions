x = int(input())
expo = 0

for i in range(1, 32):
  for j in range(2, 10):
    print(expo)
    if i**j <= x:
      expo = max(expo, i**j)
    else:
      break

print(expo)
