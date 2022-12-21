def merge(d1,d2,priority):
    if priority=='first':
        for i in d2:
            if i not in d1:
                d1[i] = d2[i]
        return d1
    if priority == 'second':
        for i in d1:
            if i not in d2:
                d2[i] = d1[i]
        return d2
d1= {1: 2, 2: 3, 3: 4}
d2 = {1: 10, 4: 15, 5:10}
print(merge(d1,d2,'first'))
#{1: 2, 2: 3, 3: 4, 4: 15, 5: 10}
#{1: 10, 4: 15, 5: 10, 2: 3, 3: 4}