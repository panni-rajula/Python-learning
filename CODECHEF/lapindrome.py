l = 'abbaab'
# for cheking palindrome
'''def palindrome(l):
    flag = False
    for i in range(len(l)):
        if l[i]!=l[len(l)-i-1]:
            flag = False
        else:
            flag = True
    return flag'''
#print(palindrome(l))


# for dividing the input
def seperate(l):
    t= len(l)//2
    if len(l)%2!=0:
        q = l[:t]
        w = l[(t)+1:]
    else :
        q = l[:t]
        w = l[t:]
    return [q,w]

#print(seperate(l))
def count(l):
    d ={}
    for i in l:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    return d


s = seperate(l)
c1 = count(s[0])
c2 = count(s[1])
if c1==c2:
    print('true')
else:
    print("false")

