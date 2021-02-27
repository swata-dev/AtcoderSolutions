h, w = map(int, input().split())
body =[]

for i in range(h):
  body.append(list(input()))

counter = 0

for i in range(h-1):
  flag = True
  for j in range(w):
    if flag and body[i][j] != body[i+1][j]:
      counter += 1
      flag = not flag
    elif not flag and body[i][j] == body[i+1][j]:
      flag = not flag

for j in range(w-1):
  flag = True
  for i in range(h):
    if flag and body[i][j] != body[i][j+1]:
      counter += 1
      flag = not flag
    elif not flag and body[i][j] == body[i][j+1]:
      flag = not flag

print(counter)