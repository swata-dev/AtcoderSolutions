n,a,b = map(int,input().split())

times = n // (a+b)
rest = n % (a+b)

print(times*a+(a if rest>=a else rest))