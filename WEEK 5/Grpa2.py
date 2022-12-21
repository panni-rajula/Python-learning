# perfect number if the sum of its divisors is equal to the number itself
def perfect(n):
    sum = 0
    for i in range(1,(int(n/2))+1):
        if n%i == 0:
            sum += i
    return sum==n
n = 6
print(perfect(n))