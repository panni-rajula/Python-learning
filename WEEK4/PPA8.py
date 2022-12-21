n = int(input())
l=[]
for i in range(n):
    l.append([])
for i in range(n):
    for j in range(n):
        l[i].append(0)
for i in range(n):
    for j  in range(n):
        if i == j:
            l[i][j]=1
print(l)