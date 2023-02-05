#  Python Classes and Objects

#  class keyword
class MyClass():
    x = 5
print(MyClass)


# MyClass create object 
class MyClass:
    x = 5
p1 = MyClass()
print(p1.x)



#use the __init__() functions to assign values name and age
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Jonn" , 36)

print(p1.name)
print(p1.age)

# The__str__() Function
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age 

p1 = Person("John", 36)
print(p1)        


# Object Methods
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)

p1 = Person("John", 36)        
p1.myfunc()


#The self Parameter
class Person:
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name 
        mysillyobject.age = age 

    def myfunc(abc):
        print("Hello my name is " + abc.name)    

p1 = Person("Fahim", 20)
p1.myfunc()

#Modify Object Properties
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)    

p1 = Person("Faysal",20)     
p1.age = 22

print(p1.age)  #overwriten
# print(p1.name)
    

# Delete Object 
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("My name is " + self.name)        

p1 = Person("Fahim", 20)
del p1.age
# print(p1.age)


# The pass method
class Person:
    pass