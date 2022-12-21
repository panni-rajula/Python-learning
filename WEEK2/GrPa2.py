x1 = int(input())
x2 = int(input())
x3 = int(input())
x4 = int(input())
x5 = int(input())
def even(x,y):
    if (x+y)%2==0:
        return True
    else:
        return False
if even(x1,x2) and even(x2,x3) and even(x3,x4) and even(x4,x5) and even(x5,x1):
    print("YES")
else:
    print("NO")