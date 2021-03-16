n = int(input())
num_list = list(map(int, input().split()))
count = 0

for i in range(len(num_list)):
  while num_list[i] % 2 == 0:
    num_list[i] /= 2
    count += 1

print(count)