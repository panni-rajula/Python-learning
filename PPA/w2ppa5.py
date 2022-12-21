x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
x3 = int(input())
m = (y2-y1)/(x2-x1)
y3 = y1 + (x3-x1)*m
if m==1:
    print("vertical")
elif m>0:
    print(m)
    print("positive slope")
elif m<0:
    print(m)
    print("negative slope")
elif m == 0:
    print("horizontal line")