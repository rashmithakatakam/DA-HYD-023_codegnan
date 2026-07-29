"""
Tokens-->variables,punctuators

VAriables--> named memory location ,its a placeholder for data
#Rules are to be followed

#MultiAssignment of vraiable

name,age,place="Rashmitha",22,"Hyderabad"
print(name,age,place)
print(name,age,place,sep=',')
print(name,age,place,sep='------>')

#a,b=2,4,5 #ValueError as too many values to unpack
#Reassigning Variables

name="codegnan"
a,b=45,1.5
print(a,b)
a,b=b,a #swapping
print(a,b,sep=',')

#a,b=c,a #nameError as c is  not defined
#print(a,b,sep=',')

#Deleting the variables-->del
#del a
#print(a)
#del a,b
#pint(a,b)

#Punctuators-->[](Lists),()(tuples),{}(Dict sets)
name="Codegnan";age=7;course="Data Analytics"
print(name,age,course)

#Datatypes-->Numeric(int,float,complex),boolean,None
        #-->Sequences-->Lists,Tuples,sets,Strings,Frozensets,mappings(dict)


#Numeric type-->int,float,complex

#int datatype-->quantity,age..
aage=7
print(age)
print(type(age))#type-->returns the dattype of object

print(type(234))

#quantity=03 #it is not allowed
#print(quantity)

#float datatype-->temp,salary,price
price=750.24;discount=2.5
print(price,discount)
print(type(price))
"""
#complex-->combination of real and imag
i2=4
data=5+i2
print(data)

data=5+2j #j is imaginary representation
print(data)
print(type(data))

#Boolean -->True/False

valid=True
print(type(valid))

error=False
print(type(error))


#TYpeCasting-->Converting one type  to another type
#python by default follows Implict Type(we need not mention the datatype)

#We will go for Explict Conversion

#Every  built-in datatype is a built-in function
int,float,complex,bool

#Typecasting --> int-->float,complex,bool

age=35
print(type(age))
b=float(age)
print(b)
c=complex(age)
print(c)
d=bool(age) #returns True for existing data
print(d)
e=bool(0)
print(e)

#Float -->typecasting
age=35.4
print(type(age))
b=int(age)
print(b)
c=complex(age)
print(c)
d=bool(age) #returns True for existing data
print(d)
e=bool(0)
print(e)


#Complex-->typecasting  -->int,float,bool
data=2+5j
print(type(data))
#b=int(data) #TypeError
#print(data)
#c=float(data)
#print(c)
d=bool(data)
print(d)
print(type(d))

d=5+4.5
print(d)

e=int(float(bool(45)))
print(e)

f=45+2.5+2+3j+False
print(f)































































