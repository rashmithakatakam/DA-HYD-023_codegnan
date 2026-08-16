'''#data=['codegnan','saketh','python','java']#input
#output should be as follows

0:codegnan
1:saketh
2:python
3:java

data = ['codegnan', 'saketh', 'python', 'java']

for i in range(len(data)):
    print(i, ":", data[i])
   
#Task:create a Nested tuple as above and work on slicing ,striding,and list functions

courses=('CSE','ECE',('EEE','MECH'),'CIVIL',[591,539])
print(courses)
print(len(courses))
#slicing
print(courses[2][-1])
print(courses[-2][-3:])
print(courses[-2][:-3])
print(courses[-1:][0])
print(courses[3][2])
#striding
print(courses[0:5:2])
print(courses[1:4:1])
print(courses[-1:5:1])
#list functions
courses[4].append(600)
print(courses)
courses[4].extend([600, 620, 650])
print(courses)
courses[4].insert(1, 550)
print(courses)
courses[4].remove(539)
print(courses)
courses[4].pop()
print(courses)
courses[4].clear()
print(courses)
'''
#Task:Take a  user input as string,do this in two ways..
'''
1)give the count of each repeating character
Test case 1: programming

r is repeating 2 times
g is repeating 2 times
m is repeating 2 times

2)
r is repeating 2 times
index=[1,4]
g is repeating 2 times
index=[3,10]
m is repeating 2 times
index=[6,7]

string = "programming"

for char in string:
    count = string.count(char)
if count > 1:
        indexes = []
for i in range(len(string)):
    if string[i] == char:
        indexes.append(i)
        print(char, "is repeating", count, "times")
        print("index =", indexes)
string = string.replace(char, "", 1)
'''


s = "programming"

for i in range(len(s)):
    if s.count(s[i]) > 1 and s.index(s[i]) == i:
        print(s[i], "is repeating", s.count(s[i]), "times")
       

string = "programming"

visited = []

for i in range(len(string)):
    char = string[i]
if char not in visited:
    count = string.count(char)
if count > 1:
    indexes = []
for j in range(len(string)):
    if string[j] == char:
        indexes.append(j)
        print(char, "is repeating", count, "times")
        print("index =", indexes)
        visited.append(char)
       
        

































