n = input()
flag = True
ans = int(n[0])

for i in range(1,len(n)):
  if n[i] != '9':
    flag = False
  ans += 9

print(ans if flag else ans-1)