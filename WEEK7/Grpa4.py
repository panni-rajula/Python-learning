n = int(input())
station_dict = dict()
for i in range(n):
    train_name= input()
    m = int(input())
    if train_name not in station_dict:
        station_dict[train_name] = dict()
    for i in range(m):
        c = input().split(',')
        station_dict[train_name][c[0]] = int(c[1])
print(dict(sorted(station_dict.items())))
'''
Mumbai Express
2
S1,10
S2,20
Chennai Express
3
S1,5
S2,10
S3,15'''