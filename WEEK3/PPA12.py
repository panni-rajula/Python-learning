a = input()
b = input()
for i in a:
    for j in b:
        if i == j:
            
            b= b.replace(j,'')
print(b)