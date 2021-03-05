import re

longest = re.findall('A.*Z', input())
print(len(longest[0]))