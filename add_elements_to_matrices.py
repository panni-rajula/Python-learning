x =int(input("enter the number of matrices you want to operate:"))
m =int(input("enter the rows:"))
n =int(input("enter the of columns:"))

'''for i in range(m):
    c.append([])
for i in range(m):
    for j in range(n):
        k = int(input(f'enter the element of {i} th row and {j} th column : '))
        c[i].append(k)
        
        
Trying to access an index that doesn't exist in a list.
Using invalid indexes in your loops.
Specifying a range that exceeds the indexes in a list when using the range() function.        
        '''
def add_elements_to_the_matrices(x): 
    c=[]
    for i in range(x):
        c.append([])
        for j in range(m):
            c[i].append([])
    for i in range(x):
        for j in range(m):
            for k in range(n):
                z = int(input(f"enter the value for the {j}'th rowt'h {k}'th column'th element in the {i}'th Matrix:"))
                c[i][j].append(z)
    return c
'''for j in range(m):
    for k in range(n):
        z = int(input("enter the values"))
        c[i][j][k] = z'''
print(add_elements_to_the_matrices(x))