'''P: a non-empty list of positive integers
Q: a non-empty list of positive integers
k: a positive integer
P[i]=k⋅Q[i]'''
P = [2,4,6]
Q = [1,2,3]
def linear(p,q,k):
    if len(p)!=len(q):
        return True
    if len(p)==0:
        return True
    if p[0]/q[0]!=k:
        return False
    return linear(p[1:],q[1:],k)
    '''for i in range(len(p)):
        if p[i]%q[i]==0:
            return True
    else:
        return False'''
print(linear(P,Q,2))
