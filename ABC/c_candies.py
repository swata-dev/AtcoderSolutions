n = int(input())
first = list(map(int, input().split()))
second = list(map(int, input().split()))

candies = 0
ans = 0

for i in range(n):
  candies = 0
  candies = sum(first[k] for k in range(0,i+1)) + sum(second[j] for j in range(i,n))
  ans = max(ans, candies)

print(ans)