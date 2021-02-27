a, b, c, x = [int(input()) for i in range(4)]
counter = []

for i in range(a+1):
  for j in range(b+1):
    for k in range(c+1):
      counter.append(500*i+100*j+50*k == x)

print(sum(counter))