s = input()
n = int(input())
str = sorted(s)
#print(str)
z= True
for n in range(n):
    w = input()
    wtr = sorted(w)
    if(len(str) == len(wtr)):
        if(str == wtr):
            print("Yes")
        else:
            print("No")
    for i in range(len(str)):
        for j in range(len(wtr)):
            if(wtr[j]==str[i]):
                z = True
            else:
                z=False
if (z == True):
    print("Yes")
else:
    print("No")