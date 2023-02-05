# Python-class-object

# Python Class/Object
Python is an object orineted programming language.

Almost everthing in Python is an object, with its properties and methods.

A Class is like an object constructor, or a "blueprint" for creating objects.


# Create a class
To create a class, use the keyword class:

Example

Create  a class named MyClass, with a property named x:

    class MyClass:
        x = 5

    print(MyClass)    


# Create Object
Now we can use the class named MyClass to create objects:

Example

Create an object named p1, and print the value of x:

    clss MyClass:
        x = 5

    p1 = MyClass()
    print(p1.x

# The __init__() Function
The examples above are classes and objects in their simplest from, and are
not really useful in real life applications.

To understand the meaning of classes we have to understand the built-in 
__init__() function.

All classes have a function called__init__(), which is always executed when 
the class is beign intiated.

Use the __init__() function to assign values to object properties, or other 
operations that are necessary to do when the object in being created:

Example

Creat a Class named Person, use the __init__() function to assign values for 
name and age:

    class Person:
         def __init__(self, name, age):
            self.name = name
            self.age = age

    p1 = Person("Fahim" 20)

    print(p1.name)
    print(p1.age)
