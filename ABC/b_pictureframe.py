h,w = map(int, input().split())
pixels = [input() for i in range(h)]

print('#'*(w+2))

for i in range(h):
  print('#'+ pixels[i] +'#')

print('#'*(w+2))