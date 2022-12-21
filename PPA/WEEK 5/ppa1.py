def fact(n):
    if n==0:
        return 1
    elif n>0:
        return n*fact(n-1)
    elif n <0:
        return -1
m = int(input())
print(fact(m))