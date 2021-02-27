n, x = map(int, input().split())

nums = list(map(int, input().split()))
ans = []

for i in range(n):
  if nums[i] != x:
    ans.append(nums[i])

print(' '.join(map(str, ans)))