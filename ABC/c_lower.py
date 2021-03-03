n = int(input())
heights = list(map(int, input().split()))
jump,distance = 0, 0

for i in range(n-1):
  if heights[i] >= heights[i+1]:
    jump += 1
  else:
    jump = 0
  distance = max(jump, distance)

print(distance)