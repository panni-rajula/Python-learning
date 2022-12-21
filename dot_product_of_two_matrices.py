c = [[[1, 2], [3, 2]], [[1, 3], [2, 1]]]
g =[1, 2]
q=[1, 3]
m = 2
n = 2
ans = 0
for i in range(len(c)):
    for j in range(len(c[i])):
        p = c[i][j]
        print(f'rows of the mega matrixs are {p}')
for i in range(m):
    ans  = ans + (g[i]*q[i])
print(ans)