t = int(input())
for i in range(t):
    n = int(input())
    x = list(map(int,input().split()))
    print(x)
    for i in range(1,len(x)-1):
        if x[i]==x[i-1] or x[i]==x[i+1]:
            x.remove(x[i])
    print(len(x))