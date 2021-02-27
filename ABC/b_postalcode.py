import re
a,b = map(int,input().split())

pattern = re.compile("[0-9]{%s}-[0-9]{%s}" % (a, b))
formatted = pattern.match(input())

print('Yes') if formatted else print('No')
