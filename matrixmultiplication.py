#we have to initialise the output matrix to add the product into that matrix
# next we have to write the function to find the produt of the rwo and column of onematrix to another
# after finding the dot product we just have to append the values into the output matrix
# initialising the output matrix
# let C be the output matrix and [m,n] be the dimension

def output_matrix(dim):
    c =[]
    for i in range(dim):
        c.append([])
    for i in range(dim):
        for j in range(dim):
            c[i].append(0)
    return c
# after initialising, we have to find the product of the row and column of the matrices to add to the output matrix 
def dot_product(u,v):
    ans =0
    dim = len(u)
    for i in range(dim):
        ans = ans+ (u[i]*v[i])
    return ans
#getting the rows of the first matrix
def row(M,i):
    #where i is the ith row of the matrix
    l =[]
    for k in range(len(M)):
        l.append(M[i][k])
    return l
# now we have to get the Ccoulumns of a matrix so that we can use the dot_product function and find the product
def column(M,j):
    #this means the j th column of the matrix M
    l = []
    for k in range(len(M)):
        l.append(M[k][j])
    return l
# now we just have to use all the functions listed above so that we can get the output
def mat_multiplication(A,B):
    c = output_matrix(dim)
    for i in range(len(A)):
        for j in range(len(B)):
            c[i][j]=dot_product(row(A,i),column(B,j))
    return c

A =[[1,2],[1,3]]
B = [[1,3],[1,2]]
dim = 2
#
print(output_matrix(dim))
print(mat_multiplication(A,B))