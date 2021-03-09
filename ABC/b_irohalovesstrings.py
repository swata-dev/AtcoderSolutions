n,l = map(int, input().split())
s_list = [input() for i in range(n)]

s_list = sorted(s_list)
ans = ''.join(s_list)
print(ans)