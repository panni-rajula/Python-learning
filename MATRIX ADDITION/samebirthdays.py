b = input()#for inputiing of names
a =input()#for inputting of birthdays
z = b.split(",")
names=[]
for i in range(len(z)):
    names.append(z[i])
#print(z)


y = a.split(",")
birthdays = []
#print(y)
for i in range(len(y)):
    birthdays.append(int(y[i]))
print(birthdays)
for i in range(len(birthdays)):
    for j in range(i+1,len(birthdays)):
        if(birthdays[i] == birthdays[j]):
            m = birthdays.index(birthdays[i])
            #print(i)
print(f"index:{i},birthday:{birthdays[i]},name:{names[i]}")