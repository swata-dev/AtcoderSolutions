n = int(input())
nums = list(map(int,input().split()))
count = 0
m = nums[0]

for i in range(n):
  m = min(nums[i], m)
  if nums[i] <= m:
    count += 1

print(count)