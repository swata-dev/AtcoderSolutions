import math
a, b = input().split()
print("Yes") if math.sqrt(float(a+b)).is_integer() else print("No")