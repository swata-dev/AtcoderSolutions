s = list(input())
alphabet = list('abcdefghijklmnopqrstuvwxyz')

for l in s:
  if l in alphabet:
    alphabet.remove(l)

if alphabet:
  print(min(alphabet))
else:
  print('None')