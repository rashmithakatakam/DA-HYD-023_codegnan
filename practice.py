'''#sum of  given numbers using for loop
price=list(map(int,input().split(',')))
total=0
for i in price:
    total=total + i
print(total)

#program to count uppercase,lowercase,digits,special
password=input("Enter password:")
upper=0
lower=0
digit=0
special=0
for ch in password:
    if ch.isupper():
        upper+=1
    elif ch.islower():
        lower+=1
    elif ch.isdigit():
        digit+=1
    else:
        special+=1
print("Uppercase",upper)
print("Lowercase",lower)
print("Digit",digit)
print("Specialcharacters",special

#Or
password=input()
upper=lower=digit=special=0
for ch in password:
      if 'A'<= ch <='Z':
           upper+=1
      elif 'a'<= ch <='z':
          lower+=1
      elif '0' <= ch <='9':
          digit+=1
      else:
          special+=1
print("Upper",upper)
print("Lower",lower)
print("Digit",digit)
print("Special",special)


#given input should change into domians
email=input("enter email:")
domain=email.split('@')[1]
print(domain)

#0r
email=input().split()
for mail in email:
    print(mail.split('@')[1])
'''

#movies should return with index






















