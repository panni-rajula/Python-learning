def pyramid(n):
    if n == 1:
        return 1
    return n  +pyramid(n-1)
print(pyramid(5))