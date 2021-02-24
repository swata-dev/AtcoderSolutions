def f(n):
  if n > 1:
    return 2*f(n//2)+1
  else:
    return 1

print(f(int(input())))