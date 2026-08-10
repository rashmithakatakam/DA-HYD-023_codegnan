'''
Strings --> Caseconversions,Searching &finding,string testing methods ,Replace,Space removal

#Searching,Finding,Replacing,Joining...
a="Codegnan"
print(len(a))
print(min(a))
print(max(a))

b=a.index('g')#it returns index position
print(b)
c=a.index('n')#it returns only the first character
print(c)
d=a.index('n',6)#it returns the next occurance
print(d)
#e=a.index('n',8)
#print(e)
#f=a.index('t')
#print(f)
g=a.index('n',1,4)
print(g)

#rindex()-->returns last occurance
b=a.rindex('g')
print(b)
c=a.rindex('n')#here 'n' is occuring at 7th index
print(c)
#d=a.rindex('n',8)#it returns value error
#print(d)


#count()-->returns the number of items object is repeating

print('Codegnan'.count('n'))
print('code'.count('w'))#it returns 0 as we don't have 'w' in 'code'
print('cakshjasaksajs'.count('a'))


#find()--> first occurance but it avoid error returns -1 if substring is not found
print('codegnan'.find('r'))
print('codegnan'.find('n'))
print('codegnan'.rfind('n'))


a='DataAnalysis'
print(len(a))
for i in a:
    #print(i)
    print(a.count(i))

a='Data'
print(len(a))
for i in a:
    #print(i)
    print(a.count(i),a.index(i))

#replacing,Splitting,Joining

#strings are immutable
a='codegnan'
#a[4]='s'
print(a.replace('g','s'))
print(a)
a=a.replace('g','s')
print(a)
print('fghijklmnopqrstuv#wxyz'.replace('#',''))
print(a.replace('x','rash'))


a='code rashmitha python'
print(len(a))
b=a.split()#by default if we have space it splits (return list)
print(b)
print(len(b))
c='code,rashmitha,python'
d=c.split()
print(d)
e=c.split(',')
print(e)

#Join()

a='code'
b='gnan'
print(a.join(b))
print(b.join(a))
print('#'.join('rashmitha'))
print(''.join('rashmitha'))

#string testing methods(boolean)
#isalpha(),isalnum(),isdigit(),isupper(),islower()...


a='codegnan123'
print(a.isalnum())#returns True for alphanumeric strings else False
b='codegnan'
print(b.isalnum())
print(a.isalpha())#returns True only for alphabets
print(a.isdigit())#returns True only for digit sting
print('8520861554'.isdigit())
print('2345'.isnumeric())#this has upper edge(numbers,fractions,romans)
print('codegnan'.startswith('c'))
print('codegnan'.startswith('g',4))
print('codegnan'.endswith('f'))


print('codegnan'.islower())#returns True for all lowercases
print('codegnan'.isupper())#returns True for all uppercases
print('codegnan python'.istitle())


#space removal --> strip()(removes leading and trailing spaces)

a='codegnan'
print(a.strip())
b=input("Enter the string:").strip().lower()
print(b)
'''

#zfill() filling with zeros as per the given numeric string
print('234'.zfill(4))
print('234'.zfill(7))
#center(),ljust(),rjust()-->Alignment of strings (check length and then modify the  width accordingly)
print('hai'.center(6))
print('hai'.center(6,'#'))

print('hai'.ljust(6,'#'))
print('hai'.rjust(6,'#'))
























































