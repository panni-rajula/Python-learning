def multiply1(a,b):
    if b == 1:
        return a
    return a + multiply1(a,b-1)
def multiply2(a,b):
    if a == 1:
        return b
    return b+ multiply2(a-1,b)
print(multiply2(1,1000))