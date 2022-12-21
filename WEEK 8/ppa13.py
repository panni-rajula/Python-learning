def zero_matrix(n):
    m=[]
    for i in range(n):
        l=[]
        for j in range(n):
            l.append(0)
        m.append(l)
    return m
def mul_mat(A,B):
    n = len(A)
    prod = zero_matrix(n)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                prod[i][j] += A[i][k] * B[k][j]
    return prod

A = [[1,2,3],[1,2,3],[1,2,3]]
B = [[1,2,3],[1,2,3],[1,2,3]]
print(mul_mat(A,B))