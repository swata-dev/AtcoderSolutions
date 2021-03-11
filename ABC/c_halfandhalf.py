a,b,c,x,y = map(int, input().split())

if c > (a+b)/2:
  print(a*x+b*y)
else:
  if 2*c < a and max(x,y) == x:
    print(c*2*x)
  elif 2*c < b and max(x,y) == y:
    print(c*2*y)
  elif max(x,y) == x:
    print(c*2*y+a*(x-y))
  else:
    print(c*2*x+b*(y-x))