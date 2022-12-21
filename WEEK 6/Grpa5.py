# Rotation of a matrix
m = [[1,2,3],[4,5,6],[7,8,9]]
trans = []
for i in range(len(m[0])):
    trans.append([])
    for j in range(len(m)):
        trans[i].append(0)
for i in range(len(m[0])):
    for j in range(len(m)):
        trans[i][j] = m[j][i]
for i in range(len(trans)):
    trans[i] = trans[i][::-1]
print(trans)
