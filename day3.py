#Numeric datatype --> int,float,complex along with boolean

#Input formatting --> Accepting input from the user--> input()

#Accepting integer from user
#by default input() accepts any input -->str
#int(input())-->will accept only integers
"""
age=int(input("enter the age:"))
print(age)
print(type(age))

#float(input()) -->accepts integers,float values
age=float(input("enter the age:"))
print(age)
print(type(age))

#Accepting string input from user

name=input("enter the name:")
print(name)
print(type(name))

#Accept group of values


marks=int(input("enter the marks:")).split()
print(marks)


#space seperated values
a=input().split()#now you enter spaces in output
print(a)
#comma seperated values
a=input("Enter the values:").split(',')
print(a)

#List of integers
marks=list(map(int,input("enter the values:").split(',')))
print(marks)

#Now we want o accept 2 values from user
age,salary=map(int,input("enter the values:").split(','))
print(age)
print(salary)

#single input -->int(input))
#two inputs -->a,b=map(int(input().split(','))
#any number result as list -->a=list(map(int,input(),split(',')))

age,salary=map(float,input("enter the values:").split(','))
print(age)
print(salary)

#group of float values
marks=list(map(float,input("enter the values:").split(',')))
print(marks)


#Accepting input from user -->int,float -->input formatting

#Operators --> operators perform operations between values(operands)
#7types -->Arithmetic,Assignment,Camparision(Relationship)
#Membership,identity,logical,Bitwise

#arithemetic operators-->Arithmetic operations
#+,-,*,/
print(5+3)
print(5-3)
print(5*3)
print(5/3)#float value
#floor division (integer division)-->returns he quotient
print(5//3)
#Modulus -->divisible rules -->returns remainder
print(5%3)
#power(exponential)
print(5**3)

#Task-->Accept integer input as length,breadth-->find the area of rectangle
#Area =length*breadth
length=12
breadth=13
print(length*breadth)

#Assignment operators --> assign the values
# =, +=,-=
a=45
print(a)
#update the value of a
a = a+5 #a+=5
print(a)
b=35
b+=a #b=b+a
print(b)
b-=5
print(b)#=b-5

#Task:*=,/=,//=,%=,**= workout
b*=5
print(b)
b/=5
print(b)
b//=5
print(b)
b%=5
print(b)
b**=5
print(b)

#Camparision operators -->we compare the values-->boolean
# == (equal to),!=(not equal to),<(less than),>(greater than)
# <=(less than or equal to)>=(greater than or equal to)

age=25
print(age==25)
print(age!=35)
print(age<25)
print(age<=25)
print(age>35)
print(age>=35)

print(-5<-1)


#membership operators -->in not in
#it checks for the existnce of an object in a collection

marks=[56,75,45,85]
print(35 in marks)
#print(35 in 355)#typeError

print(25 not in marks)
print('code' in 'codegnan')
print('$' in 'abc$frg')

#Logical operators -->logical decision making --> and.or,not
#and-->all conditions to be satified
#or-->any one condition to be satisfied

a=(25 in [25,45,65]) and 45<56
print(a)
b=45>56 or 25<=45
print(b)
c=not True
print(c)

#identity operators-->check for identity of an object -->id()

a=35
b=35
print(id(a))
print(id(b))
print(a is b)
c=a
print(id(c))
print(c is a)"""

a=[1,3,4,5]
print(id(a))
c=a
print(id(c))
print(c is a)

