x = int(input())
sum = 0
k = True
for j in range(2,x+1):
    
    for i in range(2,j):
        if j%i==0:
            k = False
    if k == True:
        sum += j
    k = True
print(sum)
################################
'''n = int(input())
sum = 0
prime = True
for i in range(2,n+1):
    for j in range (2,i):
        if i%j == 0:
        prime = False
    if prime:
        sum+=i
    prime = True
print(sum)'''