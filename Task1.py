'''#slicing with +ve,+ve
name='rashmithakatakam'
print(name[:])
print(name[5:14])
print(name[7:11])

#slicing with -ve,-ve
print(name[-13:-7])
print(name[-9:-2])
print(name[-6:])

#slicing with +ve,-ve
print(name[1:-13])
print(name[6:-3])
print(name[-8:])
'''

#striding
name='swapnakatakam'
print(name[2:9:3])
print(name[7:12:2])
print(name[5:-7:1])
print(name[1:-8:2])

#Task: A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z
#use loops and strings to return A-Z
letters = 'abcdefghijklmnopqrstuvwxyz'
for i in letters:
    print(i.upper(),end='')
