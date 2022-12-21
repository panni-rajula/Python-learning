def dot_checker(x,l):
    dummylist=[]
    if len(x) == l:
        for i in range(l):
            dummylist.append(x[i])
        x.remove(".")
        print(x)
l = int(input())
x = input()
dot_checker(x,l)