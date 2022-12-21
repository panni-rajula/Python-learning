# 1. create  an output matrix with the dimension rows of matrix A and columns of matrix B
# 2. define a function to accept two  matrices
# 3. do the dot product of the row of the first matrix and the column of the second matrix
# 4. add the dot product to the corresponding row,and column of the output matrix


# this function is for yhe square matrix
'''def output_matrix(dim):
    c =[]
    for i in  range(dim):
        c.append([])
    for i in range(dim):
        for j in range(dim):
            c[i].append(0)
    return c'''

no_of_matrices = int(input())
for i in range(no_of_matrices):
    m = int(input(f'enter the no.of rows for the {i}th matrix:'))
    n = int(input(f'enter the number of columns for the {i}th matrix:'))
A =[]
B = []
def input_matrix(m,n):
    M = []
    for i in range(m):
        A.append([])
    for i in range(m):
        for j in range(n):
            x = int(input())
            A[i].append(x)
    return M


# for the matrix which are not square
def resultant_matrix(A,B):
    c=[]
    a = len(A)
    b = len(B[0])
    for i in range(a):
        c.append([])
    for i in range(a):
        for j in range(b):
            c[i].append(0)
    return c
print(resultant_matrix(A,B))