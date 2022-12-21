'''You are given a list marks that has the marks scored by a class of students in a Mathematics test.
 Find the median marks and store it in a float variable named median. You can assume that marks is a list of float values.
You do not have to accept input from the console as it has already been provided to you. You do not have to print the output to the console.
 Input-Output is the responsibility of the autograder for this problem. Refer to PPA-11 if you are not sure how this works.'''
m = input()
ma=m.split(",")
marks =[]
median =0
for i in range(len(ma)):
    ma[i] = int(ma[i])
    marks.append(ma[i])
marks.sort()
#print(marks)
mid = len(marks) // 2
res = (marks[mid] + marks[~mid]) / 2
print(res)


