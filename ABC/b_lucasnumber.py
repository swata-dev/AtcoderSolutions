n = int(input())
lucas= [2,1]

for i in range(n):
  lucas += [lucas[i]+lucas[i+1]]

print(lucas[n])