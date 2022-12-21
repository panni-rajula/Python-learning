x = input()
y = input()
z= x.split()
dum=0
for i in range(len(z)):
    if z[i] ==y:
        dum += 1
    else:
        dum +=0
if dum>0:
    print("YES")
    print(dum)
else:
    print("NO")
