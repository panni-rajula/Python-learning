def move(fr,to):
    print("MOve from" + str(fr) + "to"+ str(to))
def adjust(n,fr,to,spr):
    if n == 1:
        move(fr,to)
    else:
        adjust(n-1,fr,spr,to)
        adjust(1,fr,to,spr)
        adjust(n-1,spr,to,fr)
fr = 1
to = 2
spr = 3
n = 5
print(adjust(n,fr,to,spr))