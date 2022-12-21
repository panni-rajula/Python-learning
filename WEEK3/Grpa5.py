x = input()
re= ''

alpha = 'abcdefghijklmnopqrstuvwxyz'
for i in alpha:
    for j in x:
        if j ==i:
            re += j
print(re)