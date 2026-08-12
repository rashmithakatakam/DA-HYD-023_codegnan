'''
sequences-->strings,lists,tuples,sets
Mapping --> Dictionary

#Lists --> collection of heterogenous elements(items)
#List --> Indexed,ordered,Mutable,Heterogenous,we use [] to store the data

marks = [35,25,21,45]
print(marks)
print(len(marks))
print(type(marks))
print(45 in marks)
#operations : indexing,slicing,striding,membership,merging,repetition

#Nested Lists --> A list inside another list
'''
names = ['codegnan',25,4.6,[45,35,25,65],'DA23',34]
'''print(len(names))
print(names[0])
print(names[3])
print(names[-3])

print(type(names[0]))
print(names[0][:4])#it returns code
print(names[0][4:])

#getb the output as cdga
print(names[0][::2])
names[0]=names[0][::-1]
print(names)

print(names[3])
print(len(names[3]))
print(names[3][2])
#Indexing,slicing --> Mutable
names[2] = 'python'
print(names)
#By indexing if we change the elements , length of collection will remain same
names[4]=['codegnan','PFS','JFS','DA','AAA','DS']
print(names)
print(len(names))
print(names[3][1:3])
print(names[4][0])
print(names[4][4:])
print(names[4][1:4])

names[2:4]='rashmitha','vijay','shiva','sravan'
print(names)
#In slicing whatever elements u pass as per logic length keeps on increasing

#o/p as follows
#['codegnan',25,'rashmitha','python','shiva','java','DA23',34]
names[3:6:2]=['python','java']
print(names)

#create a nested list with strings,lists and work on Indexing,Slicing,Striding
#added advantage if u could add string function also to it
#Lists Functions --> append(),insert(),extend(),pop(),remove(),clear()
#Index(),count(),copy(),sort(),reverse()
'''
names=['codegnan','saketh']
#append() --> inserts single element to the end of the list
names.append('data')
#print(names)
#names.append('analysis','agents')#Typeerror
names.append(['analysis','agents'])
#print(names)
#append() will always increment the length of list by 1
#print(names[3])
#names[3].append('chatgpt')#it returns None as append is applicable on list not print
print(names)

#extend() --> inserts multiple elements to the end of list

names.extend('analysis')#string will be splitted
print(names)
names.extend(['analysis'])
print(names)
names.extend([45,75,24,56])
print(names)
#names.extend(35,45)TypeError
#print(names)

#insert(index,object)-->inserts given object before index
names.insert(1,'python')
print(names)
names.insert(0,'java')
print(names)
#names.insert([1:4],['a','b'])#syntax error
#print(names)
names.insert(-1,'AAA')
print(names)

#pop(),remove(),clear()
#pop() by default last,else given index
print(names.pop())
print(names)
names.pop(2)
print(names)

#remove() we can remove a specific value
names.extend([23,14,15])
print(names)
names.remove(14)
print(names)
#names.reverse(14)#it raises valueError
del names[1:3]#del keyword will apply permanent changes
print(names)
names.clear()#clear() will remove all the elements and returns empty list
print(names)

#data=['codegnan','saketh','python','java']#input
#output should be as follows
'''
0:codegnan
1:saketh
2:python
3:java
'''


