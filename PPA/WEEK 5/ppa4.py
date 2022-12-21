def dim_equal(a,b):
    if len(a)==len(b):
        if len(a[0]) == len(b[0]):
            return True
    else:
        return False
a = [[1,2,3],[0,1,2]]
b = [[0,0,0],[1,2,3]]
print(dim_equal(a,b))