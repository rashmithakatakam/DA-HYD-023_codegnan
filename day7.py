



#for with else
'''
work_log = [0,1,1,1,0,1,0]
#result variable --> longest_streak
longest_streak = 0#target variable
current_streak = 0
for day in work_log:
    if day == 1:
        #print(day)
        current_streak = current_streak + 1
        if current_streak > longest_streak:
            longest_streak = current_streak
            print(longest_streak)
            #break
    else:
        current_streak = 0 #streak breaks
else:
    print(f'longest streak is {longest_streak}')

#in this case when the entire loop execution is done we get result of
#else block
          
#same program with break usage

work_log = [0,1,1,1,0,1,0]
#result variable --> longest_streak
longest_streak = 0#target variable
current_streak = 0
for day in work_log:
    if day == 1:
        #print(day)
        current_streak = current_streak + 1
        if current_streak > longest_streak:
            longest_streak = current_streak
            print(longest_streak)
            break
    else:
        current_streak = 0 #streak breaks
else:
    print(f'longest streak is {longest_streak}')
print("execution done")

#for-else with Notifications Scenario

notifications = [0,0,0,0]
for notification in notifications:
    if notification == 1:
        print("Unread notification")
        break
else:
    print("All caught up")

#try to take notifications from user --> list of integers

#notifications = [0,0,0,0]
notifications = list(map(int,input("Enter the values --> 0 or 1:").split(',')))
print(notifications)                            
for notification in notifications:
    if notification == 1:
        print("Unread notification")
        break
else:
    print("All caught up")
'

#while --> it relies on condition ,it will be completely executed until the condition is satisfied..

syntax while:

while <condition>:
      statements(s).....
      ..........
      ......

while True:
    print("Yes")
    
#it runs an infinite loop we need to press ctrl+c(keyboard interupt)

i=0#initialised  statement
while i<=10:
    print(i)
    i=i+1 #counter

#reverse order
    
i=10#initialised  statement
while i>=1:
    print(i)
    i=i-1  #decrement i-=1

i=0
while i<=10:
    print(10-i)
    i=i+1
'''

#banking scenario --> PIN authentication if more than 3 attempts
#Account locked..

pin = "1314"
max_attempts = 3
current_attempt = 0
while current_attempt < max_attempts:
    entered_pin = input("Entered the ATM PIN:")
    if entered_pin == pin:
        print("Login Successful")
        break
     #continue #it holds for this condition and skips to the next part of condition
    else:
        print("Entered PIN is wrong.. TRy again carefully")
        current_attempt +=1
else:
    print("Account Locked,try after 24hours..")


























    
