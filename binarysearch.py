

'''def mid(l):
    x = (0+len(l)-1)//2
    return l[x]'''
l =[1,2,3,4,5]
def binsearch(l,y):   
    begin = 0
    end = len(l)-1
    mid = (begin+end)//2
    while(end -mid>1):
        if l[mid]==y:
            return 1
        if y<l[mid]:
            end = mid-1
        if y>l[mid]:
            begin=mid+1
        if l[begin]==y or l[end]==y:
          return 1
        else:
          return 0
print(binsearch(l,5))