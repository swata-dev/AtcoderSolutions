paper = []

for i in range(3):
  paper.append(list(map(int, input().split())))

for i in range(3):
  pattern = [paper[0][i],paper[1][i],paper[2][i]]
  paper.append(pattern)

pattern = [paper[0][0],paper[1][1],paper[2][2]]
paper.append(pattern)
pattern = [paper[2][0],paper[1][1],paper[0][2]]
paper.append(pattern)

n = int(input())
count = 0

for i in range(n):
  x = int(input())
  for j in range(8):
    if x in paper[j]:
      paper[j].remove(x)
    if not paper[j]:
      count += 1
      break

print('Yes') if count != 0 else print('No')