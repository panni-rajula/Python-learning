'''def getcol(mat,n):
    col=[]
    for i in mat:
        for j in range(len(i)):
            if j == n:
                col.append(i[j])
    return col
print(getcol(mat,n))
def getrow(mat,n):
    row = []
    for i in range(len(mat)):
        if i == n:
            row.append(mat[i])
    return row[0]
print(getrow(mat,n))'''
mat = [[1,2],[3,4]]
n = 1

def get_column(mat,n):
    column=[]
    for i in range(len(mat)):
        column.append(mat[i][n])
    return column

def get_row(mat,n):
    row = []
    for j in range(len(mat[0])):
        row.append(mat[n][j])
    return row
print(get_column(mat,n))
print(get_row(mat,n))
