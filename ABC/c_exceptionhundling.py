n = int(input())
nums = [int(input()) for i in range(n)]
fixed = nums.copy()
nums.sort()

num_max = nums[n-1]
second = nums[n-2]

for i in range(n):
  if fixed[i] == num_max:
    print(second)
  else:
    print(num_max)