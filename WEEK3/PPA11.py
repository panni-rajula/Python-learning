n = int(input())
l=True
for x in range(1,n):
    for y in range(1,n):
        for z in range(1,n):
            if (x*x)+(y*y)==(z*z) and x<y<z<n:
                print(x,y,z,sep=',')
                l= False
if l:
    print("NO Solution")
    #############################
n=int(input())
c=True
for x in range(1,n):
    for y in range(1,n):
        for z in range(1,n):
            if (x*x)+(y*y)==z*z and x<y<z<n:
                print(x,y,z, sep=',')
                c=False
if c:
 print('NO SOLUTION')