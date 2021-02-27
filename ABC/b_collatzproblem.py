s = int(input())

def f(n):
  if n % 2 == 0:
    return n // 2
  return 3*n + 1

count = 0
used = set()

while True:
    if s in used:
        break
    print(s)
    used.add(s)
    count += 1
    s = f(s)

print(count+1)