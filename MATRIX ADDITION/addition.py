def matrix(m,n):
    o =[]
    for i in range(m):
        v =[]
        for j in range(n):
            x = int(input((f"[{i}][{j}]:")))
            v.append(x)
        o.append(v)
    return o
m = int(input("enter the rows"))
n = int(input("enter the columns"))
A = matrix(m,n)
B = matrix(m,n)
C =[]
for i in range(m):
    d =[]
    for j in range(n):
        y = A[i][j]+B[i][j]
        d.append(y)
    C.append(d)
print(C)

