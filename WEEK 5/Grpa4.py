m = [[1,1],[1,1]]
def is_magic(m):
    a = len(m)
    b = len(m[0])
    c_sum = 0
    r_sum = 0
    diagonal_sum = 0
    rev_diag_sum = 0
    for i in range(a):
        diagonal_sum += m[i][i]
        rev_diag_sum += m[i][a-i-1]
    if diagonal_sum != rev_diag_sum:
        return 'NO'
    for i in range(a):
        for j in range(a):
            r_sum += m[i][j]
            c_sum += m[j][i]
    if not(r_sum == c_sum == diagonal_sum):
        return 'NO'
    else:
        return 'YES'
print(is_magic(m))