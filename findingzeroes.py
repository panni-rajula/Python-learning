def minmax(a,b):
    if a<=b:
        return a,b
    return b,a
print(minmax(3,2))