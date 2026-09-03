'''
Polymorphism --> It is also one of the key feature of OOP,
Poly->many
Morph->forms
Methods with same name can take diffeent parameters(arguments->lists)
-->Method Overloading(compile ime polymorphism)
-->Method Overriding(Run-time)
-->Operator Overloading(*,+)(__add__,__str__)

Hotstar
-->Free User-->can watch the movies with advertisements
-->Premium User-->can watch premium content without advertisements 
-->VIP User -->Live content,streaming quality,premium content

#Method Overloading:

class Hotstar:
    """Understand Polymorphism"""
    def free_watch():
        print(f'user logged into hotstar..opening home page')
    def watch(self,movie):
        self.movie = movie
        print(f'User watching {self.movie}')
app = Hotstar()
app.watch("Leo")
#app.watch()it returns error as watch() is overloaded 

#-->Method usage with default arguments
# -->Method usage with variable length arguments(*args)
# -->Method usage with type of arguments

class Hotstar:
    """Method usage with default arguments"""
    def watch(self,movie=None):
        if movie is None:
            print(f'User logged into hotstar..checking..')
        else:
            self.movie=movie
            print(f'User started watching {self.movie}')
app = Hotstar()
app.watch()
app.watch("Vikram")

class Hotstar:
    """usage of *arguments"""
    def watch(self,*movies):
        print(movies)
        for movie in movies:
            self.movie=movie
            print(f'user started watching movies {self.movie}')
app=Hotstar()
app.watch()
app.watch("Vikram","leo","KGF")               

#method overloading with type of arguments usage
#Hotstar-->one m ovie at a time
        --->multiple movies at a time

class Hotstar:
    """Method Overloading with type of arguments usage"""
    def watch(self,content):
        if isinstance(content,str):
            print(f'User watching {content}')
        elif isinstance(content,list):
            print('playing Playlist')
            for movie in content:
                print(movie)
app=Hotstar()
app.watch('rash')
app.watch(['rash','vikram','leo'])

#method overriding-->it happens in the scenario of Inheritance,where if child class is having method name same as parent class thats where overriding 
# we can use super()or if we create different objects 

class Freeuser:
    """Understanding method overriding"""
    def watch(self):
        print("User logged into Homepage...")
class PremiumUser(Freeuser):
    """Using Inheritance"""
    def watch(self,movie):
        self.movie = movie
        print(f'User watching {self.movie}')
obj=PremiumUser()
obj.watch("Vikram")
obj2=Freeuser()
obj2.watch()                                         

#in above usecase we can create different objects to access same but in real scenario what if similar to subscription plans
class Freeuser:
    """Understanding method overriding"""
    def watch(self):
        print("User logged into Homepage...")
class PremiumUser(Freeuser):
    """Using Inheritance"""
    def watch(self,movie):
        super().watch()#calling superclass method
        self.movie = movie
        print(f'User watching {self.movie}')
obj=PremiumUser()
obj.watch("Vikram")
obj2=Freeuser()
obj2.watch()


#Operator Overloading --> Operators(+,-,*,/)-->operators will behave in a different way as per user defined objects....

# + (Addition,Concatination,Merging)

print(3+4)#Addition
print('code'+'gnan')#Conctination
print([23,25]+[4,5])#Merging

#print(3.__add__(4))#__add__(self,other)
a=25;b=3
print(a.__add__(b))
a=[12,3,4];b=[3,4,5]
print(a.__add__(b))#Merging
print(a.__len__())#len(a)
print(a.__mul__(2))#print([12,3,4]*2)
'''

#lets apply the above scenario Hotstar WatchHistory
'''
class WatchHistory:
    """Define the number of hours"""
    def __init__(self,hours):
        self.hours = hours
varun = WatchHistory(100)
print(varun.hours)
akash = WatchHistory(120)
print(akash.hours)
#print(varun+akash)#TypeError unsupported operation
print(varun.hours + akash.hours)
'''
#But the preferable way is usage of __add__()
class WatchHistory:
    """Define the number of hours"""
    def __init__(self,hours):
        self.hours = hours
    def __add__(self,other):
        return self.hours + other.hours
    def __str__(self):
        return f'WatchHistory is {self.hours}'    
varun = WatchHistory(300)
print(varun)#__str__()method
print(varun.hours)
akash = WatchHistory(50)
print(akash)
print(varun + akash)            
