words = ['a', 'random', 'collection', 'a', 'another', 'a', 'random']
def freq_to_words(words):
    #x=0
    d = {}
    for i in words :
        d[i] = 0
    for i in words:
        d[i] += 1
    z ={}

    for i in d:
        l =[]
        for j in d:
            if d[i] == d[j]:
                l.append(j)
        z[d[i]] = l
    return z
print(freq_to_words(words))