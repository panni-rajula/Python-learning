def search(L,k):
    if len(L)==0:
        return False
    if L[0] == k:
        return True
    else:
        return search(L[1:],k)
L = [10, 20, 30, 40, 50]
print(search(L,15))