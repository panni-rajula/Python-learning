
def matrix(m,n):
    o=[]
    for i in range(m):
        k=[]
        for j in range(n):
            v=int(input(f"value of o[{i}][{j}]:"))
            k.append(v)
        o.append(k)
    return o
m = int(input("enter the number of rows:"))
n = int(input("enter the number of columns:"))
A = matrix(m,n)
print(A)
B = matrix(m,n)
print(B)
sum = []
for i in range(m):
    t =[]
    for j in range(n):
        val = A[i][j]+B[i][j]
        t.append(val)
    sum.append(t)
print(sum)