c = [[[1, 2], [3, 2]], [[1, 3], [2, 1]]]

for i in range(len(c)):
    m = c[i]# 0,1
    row = []
    for j in range(len(m)):#01 01
        #print(f'{j} th row of {i} th matrix = {c[i][j]}')
        row .append(c[j][i])
    print(row)
   # print(row[0])
