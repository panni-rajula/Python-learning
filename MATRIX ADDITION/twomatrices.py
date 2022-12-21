from re import M


n = int(input())
#a = []
#b = []
def matrix(m,n):
    o =[]
    for i in range(m):
        v = []
        for j in range(n):
            column = int(input(f"enter o[{i}][{j}]"))
            v.append(column)
        o.append(v)
    return o
print(" matrix of a:")
#print(matrix(n,n))
print("matrix of b:")
#print(matrix(n,n))
