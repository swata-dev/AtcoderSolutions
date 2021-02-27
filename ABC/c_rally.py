n = int(input())
people = list(map(int, input().split()))
ave = round(sum(people)/n)
min_sum = 0

for i in range(n):
  min_sum += (people[i] - ave)**2

print(min_sum)