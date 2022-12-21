M = [[1,2,3],
    [4,5,6],
    [7,8,9]]
def minor_matrix(M,i,j):
    d=[]
    for k in range(len(M)):
        t = []
        if k == i:
            continue
        else:
            
            for z in range(len(M[0])):
                if z == j:
                    continue
                else:
                    t.append(M[k][j])
        d.append(t)
    return d
    '''for k in range(len(M)):
        for z in range(len(M[0])):
            d[k][z] = M[k][z]'''
print(minor_matrix(M,1,2))
