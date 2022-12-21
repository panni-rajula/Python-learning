m = [[1,2,3],[4,5,6]]
def transpose(m):
    trans = []
    for i in range(len(m[0])):
        trans.append([])
    for i in range(len(m[0])):
        for j in range(len((m))):
            trans[i].append(0)
    for i in range(len(trans)):
        for j in range(len(trans[0])):
            trans[i][j] = m[j][i]
    return trans
print(transpose(m))