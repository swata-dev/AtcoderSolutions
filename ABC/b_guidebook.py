n = int(input())
res_list = []

for i in range(n):
  s,p = input().split()
  res_list.append((s, int(p)* -1))

dictionary = {res_list[i]: i + 1 for i in range(n)}
res_list.sort()

for i in range(n):
  print(dictionary[res_list[i]])
