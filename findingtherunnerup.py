n = int(input())
arr = list(map(int,input().split()))
arr.sort()
max = arr[-1]
for i in range(len(arr)-1,-1,-1):
    if arr[i]<max:
        sec = arr[i]
        break
print(sec)