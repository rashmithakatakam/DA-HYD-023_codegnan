'''#guess the secret code using while loop

secret=1314
guess=int(input("Guess the secret code:"))
while guess != secret:
    print("Wrong code")
    guess = int(input("Try Again:"))
print("Correct code")                   

#OR
secret=1314
guess=int(input())
while guess!=secret:
    if guess < secret:
        print("too low")
    else:
        print("too high")
        guess=int(input())
print("correct guess")
        
#OTP verification
otp = "2004"
max_attempts = 7
current_attempt = 0
while current_attempt < max_attempts:
    entered_otp = input("Entered the OTP:")
    if entered_otp == otp:
        print("otp is correct")
        break
    else:
        print("Entered otp is wrong.. Try again")
        current_attempt +=1
else:
    print("otp is wrong")

#count of orders

order=input("Enter order:")
count=0
while order != "exit":
    count=count+1
    order=input("Enter order:")
print("Total orders",count)    
'''

secret="python"
current =0
max_attempts = 3
while current < max_attempts:
    a= input()
    if (a==secret):
        print("access again")
        break
    else:
        remaining = max_attempts - current
        print(f"wrong guess and you have only")
        current += 1
else:
    print("chances over")
    















