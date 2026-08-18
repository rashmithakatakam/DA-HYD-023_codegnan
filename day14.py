'''
Tokens,Datatypes-->control flow statements-->if,elif,else,for,while,break,continue...

procedure Oriented programming
Functions-->A Function is a block of code which performs a specific task
Its a reusable group of statements where we define using
def keywoed
Advantages-->Code reuseability,Code maintainability,ease of debugging,avoiding code duplication,modularity

def fname(parameters):  Function defn
   """Doc String""" Description
   statement(s).....
   .........             Function body
   return value(s)....
fname(args)  Function call


len('codegnan')
len(['poll',23])
'''

#To perform sum of given objects
'''a={1,3}
b={4,5}
print(a+b)

def add(a,b):
    """Sum of objects"""
    c=a+b
    return c
print(add(12,3))#addition
print(add('code','gnan'))#concatination
print(add([12,5],[12,34]))#Merging
c,d=map(int,input("enter the values:").split(','))
print(c,d)
print(add(c,d))
   

def add(a,b):
    """Sum of objects without return"""
    print(a+b)
add('code','gnan')
print(add(12,-34))#it returns result along with None

#usage of return

name,age,salary="rash",22,500000
def details():
    #return name,age,salary
    #return "codegnan"
    #return 23+34+45
    return  #it returns None as output
print(details())

There are five types of arguments:

--->Positionl arguments
--->Default arguments
--->keyword arguments
--->variable length arguments(*args)
--->keyword variable length arguments(**kwargs)


#Positional Arguments --> Number of arguments in function defn should
#match with function call(order has to be maintained)
#print(len(123,234))this is as per built-in len(obj) will accept one arguments

def details(name,place):
    """To store the details"""
    #name="codegnan"
    #place="hyderabad"
    #return name,place
    print(f'Name is{name}')
    print(f'Place is{place}')
#print(details("rash","codegnan"))
#print(details("bunny","vizag"))
#print(details("vizag","shyam",34))#raises Typeerror as only 2 arguments to be given
c,d=map(int,input("Enter the values").split(','))
details(c,d)


#Default arguments-->we can make arguments as default but not first argument
#as default

#def grocery(item,price=35):
#def grocery(item="cheese",price=100):#we can also make all args as default
#def grocery(item="Burger",price):#non default always follows default
    """Usage of default arguments"""
    print(f'the Item is {item} and price is {price}')

grocery("Milk",32)
#grocery(32,"Milk")
grocery("Bread")#by default we have given price as 35
#grocery("Bread",45)
grocery()#as both item and price as default arguments
'''

#keyword arguments-->whenever we want to specify the name of argument
def employee(name,salary,role,place="codegnan"):
    """keyword arguments usage"""
    print(f'Employee name is {name},role is {role} and salary is {salary},works in {place} ')
employee("rash",20000,"admin")
employee(salary=25000,role="Frontdesk",name="Asha")
employee("Akash",25000,"IT","Cognizant")
































































