#result=[]
result = dict()
for i in range(8):
    x = input().split(",")
    winner = x[0]
    no_of_won = len(x[1:])
    if winner not in result:
        result[winner]= no_of_won
for key,value in result.items():
    print(key,':',value)