
'''task : Student marks and grade analyzer
90-100-->'A'
80-89-->'B'
70-79-->'c'
60-69-->'D'
<60-->Fail
#also -ve cases should not be allowed and marks shouldnt be greater 100


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
 

marks=int(input("enter the marks (1-100):"))
if marks>0 and marks<=100:
    if marks >=90  and marks <=100:
         print("User has secured Grade A")
    if marks>80 and marks<=89:
        print("User has secured Grade B")
    if marks>70 and marks<=79:
        print("User has secured Grade C")
    if marks>60 and marks<=69:
        print("User has secured Grade D")
    if marks <60:
        print("User has failed,study again")
else:
    print("Enter only +ve values greater than 0 and less than 100")
'''

#elif keyword -->if-elif-else
'''
if <condition1>:
  statement(s)......
elif <condition2>:
  statement(s)......
elif<condition3>:
  statement(s)......
  .............
  .............
else:
    statement(s)....
    
marks = int(input("enter the student marks:"))
if marks<0 and marks>100:
    print("Entered values should be greater than 1 and less than 100")
elif marks >=90  and marks <=100:
     print("User has secured Grade A")
elif marks>80 and marks<=89:
     print("User has secured Grade B")
elif marks>70 and marks<=79:
     print("User has secured Grade C")
elif marks>60 and marks<=69:
     print("User has secured Grade D")
elif marks <60 and marks>=0:
     print("User has failed,study again")
else:
    print("No negative values")

#Task -->same usecase try with if-elif-else usage in other way

#voter eligibility checkcase --> make sure to satisfy all possible conditions
#>=18 and 100-->Access
#<18 --> no of years eligibility should tell
#negative values -->not acceptable

age=int(input("Enter the age :"))
if age>=18 and age<=100:
        print("-------- user has vote eligibility--------")
        print("--------Access Granted---------")
if age<18 and age>0:
        print("--------user still need to get vote eligibility-------")
        print("--------user need to wait for more ",(18-age),"years-------")
else:
    print("---------only +ve values and less than 100 Acceptable------")

#Prefer if-elif-else.....

#Output -->print()
#Output Formatting --> old style formatting (using commas)
#% usage (%f,%d),format() usage,fstring notation
a,b=7,9
print(a)
print(b)
print(a,b)
name="Codegnan";batch = "DataAnalysis"
print(name,batch)#by default sep is having space
print(name,batch,sep=',')
print(name,batch,sep='------->')
#end="\n",\t--->tab space
print(name,batch,end='\t')
print(a,b,end='')
print("Hydeabad")
'''
name='rashmitha';age=22;batch='DA-023';place='Hyderabad'
'''#Usage of commas
print(batch,'is in',name)#variables and msg to be separated by comma

#old style formating -->%d-->integer,%s-->string,%f-->float
salary=24253.256
print("His salary is %d"%(salary))
print("His salary is %f"%(salary))
print("His salary is %.1f"%(salary))#% if -->rounding to 1 decimal
'''
#.format() usage
print("{} is in {}".format(name,place))#order matters

#fstring usage (more recommened)

print(f'{name} is in {place}')
print(f'{"rashmitha"} is in {name}')




    
