n, k = map(int, input().split())
n -= (n // k) * k
print(min(n, abs(n - k)))