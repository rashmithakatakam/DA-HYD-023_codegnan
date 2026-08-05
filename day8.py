''''
Tokens --> keywords,Idenifiers,Liteals,Operators,Puntuators,Variables
Operators--> Numeric dat(in,float,complex),bool
Control flow --> if,elif,else,for,while
Sequences --> strings,lists,ses,tuples,mapping(dict)

#strings --> Group of characters, we use single or double or triple quotes
#for representation of strings..
#Strings are Immutable, Ordered,Indexed collection

name='Codegnan'
print(name)
print(type(name))
print(len(name))#len --> returns the number of items in container

#index() --> is used to fetch the object(position) start at 0 and ends at len(obj)
#we use [] representation
print(name[0])
print(name[5])
#print(name[25])#iIndexError-->as its out of range

#negative Indexing -->-1 to len(obj)
print(name[-1])#it returns last character
print(name[-3])
#print(name[-33])#IndexError

#slicing --> we can access group of characters(objects)
#we use [start:end]#start default --> 0,start is included,end is excluded
print(name[:])#returns entire string
print(name[0:])#it returns entire string
print(name[:4])#starts at 0th index before 4th index
print(name[1:5])
print(name[2:6])
print(name[3:7])
print(name[4:])
'''
name='python'
'''print(name[3:7])
print(name[7:3])#returns empty as strings are immutable
#Slicing is applicable from lower index to higher index
print(name[:45])#returns till end of string
print(name[45:])

print(name[-1:-5])#returns empty string
print(name[-5:-1])#starts at -5 and ends at -2
#print 'on' from above string 
print(name[4:])
print(name[4:6])
print(name[-2:])

print(name[1:-2])
print(name[2:-6])
#observe +ve,+ve,-ve,-ve & +ve,-ve all possibilities

#striding --> [start:end:step]

course='DataAnalysis'
print(len(course))
print(course[:4])
print(course[4:])
print(course[-3:])

print(course[::1])#returns all characters
print(course[::2])#includes start to end skipping1 character

print(course[1:6:3])#[1:6]-->ataAn --> [1:6:3] -->aA
print(course[2::3])#tnys
print(course[::-1])#sisylanAataD
print(course[::-2])#sslnaa

#task: Workout with all posibilities of slicing and striding on a example

name='codegnan'
#name[3]='w' #strings are immutable

#Operations on strings --> Indexing,Concatination,Repetition
print(name*3)
print('*' * 25)#repetation

#Concatination --> combing strings

data='rashmitha' + 'python' +'' + 'database'
print(data)
print('123' * 4)#Numeric String
print('code' in 'codegnan')

for i in 'codegnan':
    print(i,':')
#in above case we get every character line by line

for i in 'codegnan':
    print(i,end='')

name="dataCodegnan"
#Built-in functions --> len(),min(),max(),sorted()
print(len(name))
print(min(name))#alphabetical order (ASCII ordering)
print(ord('A'))
print(ord('a'))
print(max(name))
print(chr(97))
print(sorted(name))#returns a list by sorting all elements
'''

#methods on strings --> Case -conversion ,Finding/searching...
name='Codegnan data'
#Case-conversions --> upper().lower(),title(),capitalize()
a=name.upper()
print(a)
b=name.lower()
print(b)

#Capitalize() --> converts first letter to uppercase
c=name.capitalize()
print(c)
d=name.title()#converts every work first letter to uppercase
print(d)

#Task : A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
#use loops and strings to return A-z
