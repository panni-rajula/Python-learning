def spiral_iterative(left,right,n):
    a = left
    b = right
    for i in range(n-1):
        centre = (a+b)/2
        a,b = centre ,b
    return a
print(spiral_iterative(0,1,4)) 