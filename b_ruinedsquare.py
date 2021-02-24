x1,y1,x2,y2 = map(int,input().split())
width = x2-x1
height = y2-y1

vertices = [x2-height, y2+width, x1-height, y1+width]
print(*vertices)