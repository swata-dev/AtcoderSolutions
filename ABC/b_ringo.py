d,n = map(int, input().split())
print(n*100**d if n <= 99 else 101*100**d)