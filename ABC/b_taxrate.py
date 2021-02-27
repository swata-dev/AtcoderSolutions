import math

n = int(input())
# 税込では切り下げるので切り上げておく
x = math.ceil(n / 1.08)

if math.floor(x * 1.08) == n:
	print(x)
else:
	print(":(")