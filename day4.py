'''
Identity Opertors -->checks the identity of an object-->id()
id() is an built in  function which returns the memory location
#is,is isnot

a=5
b=a
print(id(a))
print(id(b))
c=5
print(id(c))
print(a is c)
print(5==5)

a=[1,3,5,6]
b=a
print(id(a))
print(id(b))
c=[1,3,5,6]
print(id(c))
#As we have Lists (Mutable Collection) both c and a lists will have different
#ids where as values are same
print(c is a)#output False
print(c == a)#output True
print(a is not c)#output True

#Bitwise Opertors-->we perform bitwise  operations over operands
#& (and) ,|(or),^(XOR),Shifting operators(<<,>>)
#Number number will be converted to binary format

print(5&3)#both 5  and 3 to be converted binary and bitwise and is performed

print(5|3)#bitwise OR

print(5^3)#bitwise XOR

print(5 and 3)#here and is logical operator checks for both existance
#returns 5 in above case

print(5 or 3)#returns 3 in this case

#Leftshift Operator <<,Rightshift operator >>

print(5<1)#False Camparision
print(5<<1)#Leftshift operation by 1 position
pint(5>>1)#Rightshift operation

print(15<<2)#convert 5 to binary and perform 2 times left shifting

print(15>>2)#same 2 time right shifing


#Input Formating --> input(),in(input()),float(input())
#You know-->single input
#2 or 3 inputs-->map)()
#group of integers --> list(map(int,input().split(','))

names=input("Enter the names:").split(',')
print(names)

name1,name2=map(str,input("Enter the friends name:"),split('.'))
print(name1,name2)
'''

#Tokens -->Numeric datatypes-->opeators-->flow of the program
#Control Block   Statements --> they control the flow of the program
#when to execute ,how to execute
#Conditional statements-->if,else,elif(rely on condition to be executed)
#Repetition statements(Loops)-->for,while

'''
syntax:

if <condition>:
    statement(s)...
    ........

#age=15
age=int(input("Enter he age:"))
if age >=18:
    print("Your age is:",age


age=int(input("Enter the age:"))
if age>=18 and age in [19,21,20]:
              print("Your Age is",age)
print(age)

#else keyword -->if-else

else:
    statemen(s)...

if-else usage as below:

if <conditin>:
      statement(s)....
      ......
else:
    statement(s).......
    ........



#vote eligibility-->To check his/her voter eligibility and give access...

age=int(input("Enter the age:"))
if age>=18:
    print("You have voter eligibility and age is",age)
    print("Access Granted")
else:
    age=18-age
    #print("You dont have eligibility as your age is :",age,"years")
    print("You need to wait for more",age,"years")

#same case let's use only nested -->if,else
age=int(input("Enter the age:"))
if age>0:
    if age>=18:
        print("You have voter eligibility and age is",age)
        print("Access Granted")
    else:
        age=18-age
        #print("You dont have eligibility as your age is :",age,"years")
        print("You need to wait for more",age,"years")
else:
    print("You have entered -ve values/zero enter only +ve")

task : Student marks and grade analyzer
90-100-->'A'
80-89-->'B'
70-79-->'c'
60-69-->'D'
<60-->Fail
#also -ve cases should not be allowed and marks shouldnt be greater 100
'''

marks=int(input("Enter the marks:"))
if marks < 0 or marks >100:
    print("invalid marks! please enter marks between o to 100")
elif marks >= 90:
    print("A")
elif marks >= 80:
    print("B")
elif marks >= 70:
    print("C")
elif marks >= 60:
    print("D")
else:
    print("Fail")


marks=int(input("Enter the marks:"))
if marks < 0 or marks >100:
    print("invalid marks! please enter marks between o to 100")
if marks >= 90:
    print("A")
if marks >= 80:
    print("B")
if marks >= 70:
    print("C")
if marks >= 60:
    print("D")
else:
    print("Fail" )  
    
    



    
    
              

