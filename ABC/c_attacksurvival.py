n,k,q = map(int, input().split())
answers = [int(input()) for i in range(q)]

participants =[k-q for i in range(n)]

for i in range(q):
  participants[answers[i]-1] += 1
for i in range(n):
  print('Yes' if participants[i] > 0 else 'No')
