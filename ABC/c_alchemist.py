n = int(input())
ingredients = list(map(int,input().split()))
ingredients = sorted(ingredients)

for i in range(n-1):
   ingredients[0] = ((ingredients[0]+ingredients[1])/2)
   del ingredients[1]

print(*ingredients)