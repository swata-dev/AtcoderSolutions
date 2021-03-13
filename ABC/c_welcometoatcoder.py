n,m = map(int, input().split())
correct = [0]*n
wrong = [0]*n
penalty = 0

for i in range(m):
  q,s = input().split()
  q = int(q) - 1
  if correct[q] == 0 and s =='AC':
    correct[q] = 1
    penalty += wrong[q]
  wrong[q]+= 1

print(sum(correct), penalty)
