def binarysearch(l,k,begin,end):
    if begin == end and l[begin]==k:
        return 1
    if l[begin]==k or l[end]==k:
        return 1
    
    mid = (begin+end)//2
    if mid>k:
        end = mid-1
    if mid<k:
        begin= mid+1
    if l[mid]==k:
       return 1
    if end-begin<0:
        return 0
    return binarysearch(l,k,begin,end)
l = [1,2,3,4365]
print(binarysearch(l,56,0,len(l)-1))