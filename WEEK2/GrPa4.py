person1=input()
dob1=input()#10-03-1990
person2=input()
dob2=input()#18-12-1987

if (int(dob1[-1:-5]>dob1[-1:-5])):
    print(person1)
elif (int(dob1[-1:-5]<dob1[-1:-5])):
    print(person2)
elif (int(dob1[-1:-5]==dob1[-1:-5])):
    if (int(dob1[-6:-8]>dob1[-6:-8])):
        print(person1)
    elif (int(dob1[-6:-8]<dob1[-6:-8])):
        print(person2)
    elif (int(dob1[-6:-8]==dob1[-6:-8])):
        if (int(dob1[0:2])>int(dob2[0:2])):
            print(person1)
        elif (int(dob1[0:2])<int(dob2[0:2])):
            print(person2)
        elif (int(dob1[0:2])==int(dob2[0:2])):
            if person1<person2:
                print(person1)
            elif person1>person2:
                print(person2)
