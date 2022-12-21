def insert(L,x):
    if len(L)>0:
        if x<L[0]:
            return [x] + L[0:]
        else:
            return [L[0]]+ insert(L[1:],x)
    else:
        return [x]
L = [1,2,3,5,6,8]
print(insert(L,4))