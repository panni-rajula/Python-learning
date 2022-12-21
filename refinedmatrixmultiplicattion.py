#we have to initialise the output matrix to add the product into that matrix
# next we have to write the function to find the produt of the rwo and column of onematrix to another
# after finding the dot product we just have to append the values into the output matrix
# initialising the output matrix
# let C be the output matrix and [m,n] be the dimension


X = int(input("enter the number of matrices you want to operate:"))




# X is the no.of matrices and we use the below function to ge the dimension for each of the matrix 
def accept_the_matrices_dimension(X):
    rows = []
    columns = []
    for i in range(X):
        m = int(input(f'enter rows of{i}th :'))
        n = int(input(f'enter the columns{i}th :'))
        # print(m,n)
        rows.append(m)
        columns.appen(n)
    rows_columns=[]
    a = rows
    b = columns
    rows_columns.append(a)
    rows_columns.append(b)
    return rows_columns

# after we have done with the input of the dimensions of the matrices we now take the input of the matrices
def add_elements_to_the_matrices(X): 
    c=[] # the list c stores the matrices for which th einputs are given. So the list c is a list of matrices!!
    for i in range(X):
        c.append([]) # here we are appending the no.of empty lists equal to the no.of matrices
        for j in range(m):
            c[i].append([])
    for i in range(X):
        for j in range(m):
            for k in range(n):
                z = int(input(f"enter the value for the {j}'th rowt'h {k}'th column'th element in the {i}'th Matrix:"))
                c[i][j].append(z)
    return c
# here we are initialising an output matrix where it is filled with 0's
def output_matrix(X):
    c =[]
    for i in range(X):
        c.append([])
        for j in range(m):
            c[i].append([])
    for i in range(x):
        for j in range(m):
            for k in range(n):
                c[i][j].append(0)
    return c
###################################################################################################################
'''def output_matrix(dim):
    c =[]
    for i in range(dim):
        c.append([])
    for i in range(dim):
        for j in range(dim):
            c[i].append(0)
    return c'''
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

#
print(output_matrix(dim))
print(mat_multiplication(A,B))