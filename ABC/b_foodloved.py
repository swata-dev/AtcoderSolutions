n,m = map(int,input().split())
likes = []

for i in range(n):
  favo = list(map(str, input().split()))
  del favo[0]
  likes.append(favo)

true = 0

for j in range(1,m+1):
  count = 0
  for i in range(n):
    if str(j) in likes[i]:
      count+=1
  if count == n:
    true += 1

print(true)
