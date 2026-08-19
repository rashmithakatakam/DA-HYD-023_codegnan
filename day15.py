'''
Functions --> variable length arguments(*args)
          --> keyword variable length arguments(**kwargs)

Variable length arguments --> The number of positional arguments are not limit
we can pass anny number of positional arguments,but we need to use the * representation,
data is stored in tuple.


def sample(*args):
    """Simple demo for *args"""
    print(args)
    print(type(args))
sample()#no arguments
sample(1,3,5,6)#any number
sample('codegnan','rash',23)
details=[24,45,35,65]
sample(details)#passing a collection
sample(*details)#unpacking values from collection

#* is used for unpacking the values from collection
a,b,c=13,4,'da'
print(a,b,c)
#a,*b,c='python','codegnan',23,45,9,7,'data'
#a,b,*c='python','codegnan',23,45,9,7,'data'
a,b,*c=34,'codegnan'
print(a)
print(b)
print(c)
c.extend([23,45,6,7])
print(c)

#Task --> we wanted to calculate the sum of given objects using Function
def add(*a):
    """sum of given objects"""
    print(a)
    print(type(a))
    #take output variable as result
    result=0
    for i in a:
        #print(i)
        #if type(i) == int or type(i) == float:
        if type(i) in (int,float,complex):
            #print(i)
            result=result+i
    return result
#print(add())
#print(add(12,3,4,5))
#print(add(1,2,3,4.5))
#print(add(3,4,5,'poll','dear',45,4.5))
#print(add(23,4,5.5,2+4j,56,'code',23))
b=list(map(int,input("Enter the values:").split(',')))
#print(add(*b))#* is used to unpack the values from collection
#print(b)
print(*b)#it returns each value side by side
for i in b:
    print(i,end='')#same as here
#keyword variable length arguments --> we can pass any number of keyword
arguments we use **  representation,dat is stored in dictionary

def details(**kwargs):
    """usage of **kwargs demo"""
    print(kwargs)
    print(type(kwargs))
details()#returns empty dictionary
#details(2,3,4,6,)#raises TypeError
details(name="codegnan",place="hyd",batch="da")
batch={'number':'da23','place':'hyd'}
details(**batch)
'''

#Now let us include both of them into a function
def sample(*a,**b):
    """usage of both variable length and keyword variable length args"""
    result=0
    for i in a:
        if type(i) in (int,float,complex):
            result=result + i
    print(result)
    for key,value in b.items():
        print(f'key is {key}')
        print(f'value is {value}')
sample(2,4,5,'police','codegnan',3.5,name="codegnan",place="hyd",batch="da23")

#sample(name="codegnan",23,ids=23445)#positional args follows keyword args






