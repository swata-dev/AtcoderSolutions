n = int(input())
candidates = {}
ans = []
 
for i in range(n):
  v = input()
  if not v in candidates:
    candidates[v] = 1
  else:
    candidates[v] += 1
 
cnt = 0
for i in candidates:
  cnt = max(cnt,candidates[i])
t = []
for i in candidates:
  if candidates[i] == cnt:
    t.append(i)
 
t.sort()
 
for i in range(len(t)):
  print(t[i])