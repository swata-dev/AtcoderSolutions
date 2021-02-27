n = int(input())
s = list(input())
count = 0
maxim = 0

for sign in s:
  if sign == "I":
    count +=1
  else:
    count -=1
  maxim = max(maxim, count)

print(maxim)