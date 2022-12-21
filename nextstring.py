alpha='abcdefghijklmnopqrstuvwxyz'
s = 'india'
x=''
'''for letter in s:
    w = alpha.index(letter)
    x = x+ alpha[w+1]'''
z = 0
while z<len(s):
    y= alpha.index(s[z])
    x += alpha[y+1]
    z+=1
print(x)
