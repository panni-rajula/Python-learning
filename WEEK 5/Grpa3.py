#The distance between two letters in the English alphabet is one more than the number of letters between them
def distance(w1,w2):
    l = 'abcdefghijklmnopqrstuvwxyz'
    x=0
    if len(w1)!=len(w2):
        return -1
    elif len(w1)==len(w2):
        for i in range(len(w1)):
            x += abs(l.index(w1[i])-l.index(w2[i]))
    return x
w1 = 'dog'
w2 = 'cat'
print(distance(w1,w2))