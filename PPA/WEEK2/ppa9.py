n = int(input())
x1 = int(input())
x2 = int(input())
x3 = int(input())
if (x1!=0 and x2!=0 and x3!=0) and (x1!=x2 and x1!=x3 and x2!=x3) and(x1+x2+x3==n):
   print("FAIR")
else:
    print("UNFAIR")