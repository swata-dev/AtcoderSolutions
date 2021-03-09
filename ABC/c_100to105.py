x = int(input())
k = x // 100

print(1 if k*100 <= x <= k*105 else 0)