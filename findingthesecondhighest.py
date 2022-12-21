    for i in range(int(input())):
        k=[]
        name = input()
        score = float(input())
        k.append(name)
        k.append(score)
        scores.append(score)
        d.append(k)
    scores.sort()
    nrscores=[]
    for k in scores:
        if k not in nrscores:
            nrscores.append(k)
    sec_min= nrscores[1]
    for i in range(len(d)):
        if d[i][1]==sec_min:
            print(d[i][0])

