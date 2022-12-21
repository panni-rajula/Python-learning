def collatz(n):
    if n == 2:
        return 1
    if n%2!=0:
        return 1+ collatz((3*n)+1)
    if n%2==0:
        return 1+ collatz(n/2)
print(collatz(10))