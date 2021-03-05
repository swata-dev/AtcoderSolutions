o = input()
e = input()
password = []

for i in range(len(e)):
  password.append(o[i]+e[i])
if len(o) != len(e):
  password.append(o[-1])

password = ''.join(password)
print(password)