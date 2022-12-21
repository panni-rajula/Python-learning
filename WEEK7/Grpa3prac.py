M = [[1,2,3],
    [4,5,6],
    [7,8,9]]
def minor_matrix(M,a,b):
    d = []
    for i in range(len(M)):
        t =[]
        if i == a:
            continue
        else:
            for j in range(len(M[0])):
                if j == b:
                    continue
                else:
                    t.append(M[i][j])
        d.append(t)
    return d
print(minor_matrix(M,0,0))