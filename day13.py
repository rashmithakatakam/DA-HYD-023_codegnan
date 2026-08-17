'''
Mapping --> Dictionary -->Collection of key-value pairs used to store
related data --> JSON,API's,database records

dict() --> data={}-->data={key:value}
Dictionary is Mutable,Indexed through keys,Ordered,heterogenous,
keys must be unique(int,strings,float values)
'''
details={}
print(type(details))

details={'Id':'CGH4022','Name':'Manasa','Gender':'F','Age':20,'Batch':'DA23','Place':'HYD'}
print(details)
print(len(details))

#Access the data from dictionary
#details[0] #key error
'''
print(details.keys())#it returns keys from the dictionary
print(details['Id'],details['Name'])
#if key name is not matching / invalid
#print(details['Marks'])#KeyError as marks is not present
details['Marks']=[]
print(details)
print(type(details['Marks']))

details['Marks'].append(20)
print(details)

details['Marks'].extend([15,20,25,20,20])
print(details)

#Create a key-value pair of practice session
details ['PS']=('Tuesday','Thursday','Saturday')
print(details.keys())

#Access 3rd day marks of subject
print(details['Marks'][2])

#Accessing 2nd day of practice session
print(details['PS'][1])
details['MI']=('Monday','Wednesday','Friday')
#Operations --> mutable,indexing through  keys,membership

print('Wednesday' in details)
print('MI' in details)#returns True as we have MI as key
for i in details:
    print(i)#returns keys one by one

for i in details.keys():
    print(f'key={i}')
    print(f'value={details[i]}')

#keys()-->returns keys from the dictionary

for i in details.values():#returns value from dictionary
    print(i)

for i in details.items():#returns a key-value pair
    print(i)

for key,value in details.items():
    print(f'key is {key}')
    print(f'value is {value}')


#update()--> updating the dictionary with key-value pairs
details.update({'Marks':[],'PS':('Tuesday','Thursday','Saturday')})
print(details)
#details['Marks'].extend([25,30,25])
#print(details)
marks=list(map(int,input("Enter the mrks:").split(',')))
print(marks)
details['Marks'].extend(marks)
print(details)
'''
print(details.keys())
print(details.get('Name'))
print(details.get('Branch'))#it returns None as we don't have Branch as key
print(details.keys())

details.setdefault('Branch','ECE')#if key is not present it inserts into dict
print(details)
details['Branch']='CSE'
print(details)

print(details.setdefault('Name'))#it can't update the key which is already exist
print(details.keys())

print(details.pop('Branch'))#we need to mention key
print(details.keys())

print(details.popitem())#removes and return a key,value pair as a 2-tuple
print(details.popitem())
print(details.popitem())

del details['Id']
print(details.keys())

details.clear()#removes all elements from D
print(details)


#fromkeys()

data=['saketh','sai','data']
b=dict.fromkeys(data)#creates a dict but value set is None
print(b)
b['saketh']=31
print(b)
c=dict.fromkeys(['CGH1234','CGH2345'],['code','gnan'])
print(c)

#task:create a dictionary with your personal details,similar to your
#codegnan profile


















