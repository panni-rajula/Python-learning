n = int(input())
for i in range(n+1):
    for j in range(1,i+2):
        print(j,end=' ')
    print()
for i in range(n+1,0,-1):
    for k in range(i+1):
        print(k,end=' ')
        k = k-1
    print()
