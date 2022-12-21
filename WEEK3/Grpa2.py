n = int(input())
k = True
for i in range(2,n+1):
#    if n%i == 0:
        
        for j in range(2,i):
            if i%j==0:
                k = False
            #    break
    
        if k:
            print(i)