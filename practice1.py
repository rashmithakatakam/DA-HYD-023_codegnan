'''#movies should return with index
movies=input().split()
i=1
for movie in movies:
    print(i,".",movie,sep="")
    i=i+1

 #fibanocci series
n=int(input("Enter the number of terms:"))
a=0
b=1
for i in range(n):
    print(a,end="")
    c=a+b
    a=b
    b=c      


#fibanocci using while loop
n=int(input("Enter he number of terms:"))
a=0
b=1
i=0

while i<=n:
    print(a,end="")
    c=a+b
    a=b
    b=c
    i=i+1
    

#write a python program to calculate the innings of a batsman and count the boundaries,dotballs,and total score
#for loop
runs = [4,6,1,0,2,4,0,6]
Total_score = 0
boundaries = 0
dotballs = 0
for i in runs:
    Total_score = Total_score +i
    if i == 4 or i == 6:
        boundaries = boundaries + 1
    elif i == 0:
        dotballs = dotballs + 1
print("Total_score",Total_score)
print("Boundaries",boundaries)
print("Dotballs",dotballs)

#phonelock pattern using while loop
pin = "1314"
max_attempts = 5
current_attempt = 0
while current_attempt < max_attempts:
    entered_pin = input("Entered the phone PIN:")
    if entered_pin == pin:
        print("lock is opened")
        break
    else:
        print("Entered PIN is wrong.. TRy again carefully")
        current_attempt +=1
else:
    print("phone is locked")
'''   
#atm verification
pin = "1314"
max_attempts = 3
current_attempt = 0
while current_attempt < max_attempts:
    entered_pin = input("Entered the ATM PIN:")
    if entered_pin == pin:
        print("Login Successful")
        break
    else:
        print("Entered PIN is wrong.. TRy again carefully")
        current_attempt +=1
else:
    print("Account Locked")
