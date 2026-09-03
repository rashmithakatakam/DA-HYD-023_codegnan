'''class Father:
    """Usage of Constructor in Single Inheritance""" 
    def __init__(self):
        self.property = property
    def father_property(self):
        print(f'Father property is{self.property}')
#class Kid(Father):
    #pass
class Kid(Father):
    """Now child class will have Constructor"""
    def __init__(self,cash,property):
        self.cash = cash
        super().__init__ (property)
    def Kid_property(self):
        print(f'kid property is{self.cash}') 
        print(f'kid Final property is {self.cash + self.property}')       
obj=Kid(250000,1000000) 
obj.Kid_property() 
obj.father_property()

#what child clss is having same method name as 
# parent class --> Method Overriding
# Area ofsquare/rectangle
 
class Rectangle:
    """Method Overriding usage"""
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def area(self):
        print(f'Area of Rectangle is {self.x *self.y}')
class Square(Rectangle):
    def __init__(self,x):
        self.x=x
    def area(self):
        print(f'Area of Square is {self.x**2}')
obj=Square(6) 
obj.area()                     

class Square:
    """Method Overriding usage"""
    def __init__(self,x):
        self.x=x
    def area(self):
        print(f'Area of square is {self.x**2}')
class Rectangle(Square):
    def __init__(self,x,y):
        self.y=y
        super().__init__(x)
    def area(self):
        super().area()
        print(f'Area of Rectangle is {self.x*self.y}')
x,y = map(int,input("Enter the values:").split(','))       
obj = Rectangle(x,y)
obj.area()
''' 
#Multiple Inheritnce
'''
class Parent1:
    ........
class Prent2:
    ........
class Child(Parent1,Parent2):
    .....


class User:
    """First Parent class with User features"""
    def voice_call(self):
        print('Making voice calls')
class Notifications:
    def notifications(self):
        print('Sending Notifications')
class PremiumUser(User,Notifications):
    def  verification_badge(self):
        print("Blue Tick verification done")   
user =PremiumUser()
user.verification_badge()
user.voice_call()
user.notifications()            
'''
#Multilevel Inheritance-->level by level
'''
class GrandParent:
    ........
class Parent(GrandParent):
    ........
class Child(Parent):
    .....
''' 
class User:
    """Multilevel Inheritance usage """
    def video_call(self):
        print('Making video calls')
class BusinessUser(User):
    def create_catalog(self):
        print('Displaying product catalog')
class VerifiedBusinessUser(BusinessUser):
    def verification_badge(self):
        print('Blue tick verification done')
obj=VerifiedBusinessUser()
obj.create_catalog()                      

#Hybrid Inheritance
class Person:
    def details(self):
        print("Person details")


class Student(Person):
    def study(self):
        print("Student is studying")


class Teacher(Person):
    def teach(self):
        print("Teacher is teaching")


class ClassMonitor(Student, Teacher):
    def monitor(self):
        print("Monitor is managing the class")


obj = ClassMonitor()

obj.details()
obj.study()
obj.teach()
obj.monitor() 

#Hierarchical  Inheritance

class Animal:
    def eat(self):
        print("Animal is eating")


class Dog(Animal):
    def bark(self):
        print("Dog is barking")


class Cat(Animal):
    def meow(self):
        print("Cat is meowing")


d = Dog()
d.eat()
d.bark()

c = Cat()
c.eat()
c.meow()