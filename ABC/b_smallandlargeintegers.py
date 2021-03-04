a,b,k = map(int, input().split())
num_list = [a+i for i in range(k)]
num_list += [b-i for i in range(k-1,-1,-1)]

if b-a+1 > k*2:
  for i in num_list:
    print(i)
  # for i in range(a,a+k):
  #   print(i)
  # for i in range(b-k+1,b+1):
  #   print(i)
else:
  for i in range(a,b+1):
    print(i)