def non_decreasing(L):
    if len(L)<=1:
        return True
    if L[-1]<L[-2]:
        return False
    return non_decreasing(L[:-1])


L = [10, 1, 100, 1000, 10000]
print(non_decreasing(L))