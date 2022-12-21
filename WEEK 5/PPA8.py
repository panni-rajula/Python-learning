n = 10
def fib(n):
    l = []
    for i in range(n):
        l.append(0)
    l[0] = l[1] = 1
    for i in range(2,n):
        l[i] = l[i-1] + l[i-2]
    return l
print(fib(n))