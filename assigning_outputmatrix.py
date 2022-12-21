x =int(input("enter the number of matrices you want to operate:"))
m =int(input("enter the rows:"))
n =int(input("enter the of columns:"))
def output_matrix(x):
    c =[]
    for i in range(x):
        c.append([])
        for j in range(m):
            c[i].append([])
    for i in range(x):
        for j in range(m):
            for k in range(n):
                c[i][j].append(0)
    return c
    