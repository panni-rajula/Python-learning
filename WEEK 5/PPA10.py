def insert(L,x):
    L.append(x)
    for i in range(len(L)):
        for j in range(i+1,len(L)):
            if L[j]<L[i]:
                L[i],L[j]= L[j],L[i]
    return L
L = [1,2,3,4,5]
x = 7
print(insert(L,x))