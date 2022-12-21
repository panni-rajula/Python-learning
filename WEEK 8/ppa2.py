'''Write a recursive function named multiply accepts two positive integers aa and bb as argument and returns their product. You can only use ++ and -− operators. You are not allowed to use the *∗ symbol anywhere in your code!'''
def factorial(n):
    if n ==0:
        return 1
    return n * factorial(n-1)
print(factorial(4))