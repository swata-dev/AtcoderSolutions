import re

s = input()
words = ["dream", "dreamer", "erase", "eraser"]

if re.match("^(dream|dreamer|erase|eraser)+$", s):
  print("YES")
else:
  print("NO")
