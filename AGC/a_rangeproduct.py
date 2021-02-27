import numpy as np

a,b = map(int, input().split())
count = 0

for i in range(a, b+1):
  if i == 0:
    print('Zero')
    exit()
  if np.sign(i) == -1:
    count += 1

if count % 2 == 0:
  print('Positive')
else:
  print('Negative')