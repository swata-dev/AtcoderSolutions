n = int(input())
difficulty = list(map(int, input().split()))
difficulty = sorted(difficulty)

if difficulty[int(n/2)]-difficulty[int(n/2-1)] == 0:
  print(0)
else:
  print(difficulty[int(n/2)]-difficulty[int(n/2-1)])